require "bootcamp"

describe "Bootcamp" do
  let(:bootcamp) { Bootcamp.new("Map Academy", "Anyone can be a cartographer.", 6) }

  describe "PART 1" do
    describe "#initialize" do
      it "should accept a name (string), slogan (string), and student_capacity (number) as args" do
        bootcamp
      end

      it "should set the instance variables @name, @slogan, and @student_capacity" do
        expect(bootcamp.instance_variable_get(:@name)).to eq("Map Academy")
        expect(bootcamp.instance_variable_get(:@slogan)).to eq("Anyone can be a cartographer.")
        expect(bootcamp.instance_variable_get(:@student_capacity)).to eq(6)
      end

      it "should set the instance variables @teachers and @students to empty arrays" do
        expect(bootcamp.instance_variable_get(:@teachers)).to eq([])
        expect(bootcamp.instance_variable_get(:@students)).to eq([])
      end

      it "should set the instance variable @grades to an empty hash where the default values are distinct empty arrays" do
        grades = bootcamp.instance_variable_get(:@grades)

        expect(grades).to eq({})
        expect(grades["Alice"]).to eq([])
        expect(grades["Bob"]).to eq([])

        grades["Alice"] << 42
        expect(grades["Alice"]).to eq([42])
        expect(grades["Bob"]).to eq([])
      end
    end

    describe "#name" do
      it "should get (return) the bootcamp's @name" do
        expect(bootcamp.name).to be(bootcamp.instance_variable_get(:@name))
      end
    end

    describe "#slogan" do
      it "should get (return) the bootcamp's @slogan" do
        expect(bootcamp.slogan).to be(bootcamp.instance_variable_get(:@slogan))
      end
    end

    describe "#teachers" do
      it "should get (return) the bootcamp's @teachers" do
        expect(bootcamp.teachers).to be(bootcamp.instance_variable_get(:@teachers))
      end
    end

    describe "#students" do
      it "should get (return) the bootcamp's @students" do
        expect(bootcamp.students).to be(bootcamp.instance_variable_get(:@students))
      end
    end

    describe "#hire" do
      it "should accept a teacher (string) and add them to the end of @teachers" do
        bootcamp.hire("Jeff")
        expect(bootcamp.teachers).to eq(["Jeff"])

        bootcamp.hire("Matthias")
        expect(bootcamp.teachers).to eq(["Jeff", "Matthias"])
      end
    end

    describe "#enroll" do
      it "should accept a student (string) as an arg" do
        bootcamp.enroll("Alice")
      end

      context "when the number of enrolled students is below @student_capacity" do
        it "should add the student to @students" do
          bootcamp.enroll("Alice")
          expect(bootcamp.students).to eq(["Alice"])
          bootcamp.enroll("Bob")
          expect(bootcamp.students).to eq(["Alice", "Bob"])
        end

        it "should return true since the enrollment was successful" do
          expect(bootcamp.enroll("student one")).to eq(true)
          expect(bootcamp.enroll("student two")).to eq(true)
        end
      end

      context "when the number of enrolled students is at @student_capacity" do
        it "should not add the student to @students" do
          8.times { bootcamp.enroll("Alice") }
          expect(bootcamp.students.length).to eq(6)
        end

        it "should return false since the enrollment was not successful" do
          expect(bootcamp.enroll("student one")).to eq(true)
          expect(bootcamp.enroll("student two")).to eq(true)
          expect(bootcamp.enroll("student three")).to eq(true)
          expect(bootcamp.enroll("student four")).to eq(true)
          expect(bootcamp.enroll("student five")).to eq(true)
          expect(bootcamp.enroll("student six")).to eq(true)
          expect(bootcamp.enroll("student seven")).to eq(false)
          expect(bootcamp.enroll("student eight")).to eq(false)
        end
      end
    end

    describe "#enrolled?" do
      it "should accept a student (string) and return a boolean indicating whether the student is enrolled in the bootcamp" do
        bootcamp.enroll("Alice")
        expect(bootcamp.enrolled?("Alice")).to eq(true)
        expect(bootcamp.enrolled?("Bob")).to eq(false)
      end
    end
  end

  describe "PART 2" do
    describe "#student_to_teacher_ratio" do
      it "should return an integer representing the ratio between # students to 1 teacher rounded down to the nearest integer" do
        bootcamp.hire("Jeff")
        bootcamp.hire("Matthias")
        bootcamp.enroll("student one")
        bootcamp.enroll("student two")
        bootcamp.enroll("student three")
        bootcamp.enroll("student four")
        expect(bootcamp.student_to_teacher_ratio).to eq(2)

        bootcamp.enroll("student five")
        expect(bootcamp.student_to_teacher_ratio).to eq(2)

        bootcamp.enroll("student six")
        expect(bootcamp.student_to_teacher_ratio).to eq(3)
      end
    end

    describe "#add_grade" do
      it "should accept a student (string) and a grade (number) and add that grade to the student's grades array inside of the @grades hash" do
        bootcamp.add_grade("Alice", 100)
      end

      context "when the student is already enrolled" do
        it "should add the grade to the student's grades array inside of the @grades hash" do
          bootcamp.enroll("Alice")
          bootcamp.enroll("Bob")
          bootcamp.add_grade("Alice", 100)
          bootcamp.add_grade("Alice", 75)
          bootcamp.add_grade("Bob", 87)
          expect(bootcamp.instance_variable_get(:@grades)).to eq({"Alice"=>[100, 75], "Bob"=>[87]})
        end

        it "should return true" do
          bootcamp.enroll("Alice")
          expect(bootcamp.add_grade("Alice", 100)).to eq(true)

          bootcamp.enroll("Bob")
          expect(bootcamp.add_grade("Bob", 87)).to eq(true)
        end
      end

      context "when the student is not enrolled in the bootcamp" do
        it "should not add the grade" do
          bootcamp.enroll("Alice")
          bootcamp.add_grade("Alice", 100)
          bootcamp.add_grade("Bob", 87)
          expect(bootcamp.instance_variable_get(:@grades)).to eq({"Alice"=>[100]})
        end

        it "should return false" do
          expect(bootcamp.add_grade("Alice", 100)).to eq(false)
          expect(bootcamp.add_grade("Bob", 87)).to eq(false)
        end
      end
    end

    describe "#num_grades" do
      it "should accept a student (string) and return the number of grades they have" do
        bootcamp.enroll("Alice")
        bootcamp.add_grade("Alice", 100)
        bootcamp.add_grade("Alice", 75)
        expect(bootcamp.num_grades("Alice")).to eq(2)

        bootcamp.enroll("Bob")
        bootcamp.add_grade("Bob", 80)
        expect(bootcamp.num_grades("Bob")).to eq(1)
      end
    end

    describe "#average_grade" do
      it "should accept a student (string) and return a number representing their average grade rounded down to the nearest integer" do
        bootcamp.enroll("Alice")
        bootcamp.add_grade("Alice", 100)
        bootcamp.add_grade("Alice", 75)
        expect(bootcamp.average_grade("Alice")).to eq(87)

        bootcamp.enroll("Bob")
        bootcamp.add_grade("Bob", 80)
        expect(bootcamp.average_grade("Bob")).to eq(80)
      end

      it "should return nil if the student has no grades or is not enrolled" do
        bootcamp.enroll("Bob")
        expect(bootcamp.average_grade("Bob")).to eq(nil)

        expect(bootcamp.average_grade("Alice")).to eq(nil)
      end
    end
  end
end
