
# `if let`

```rust

if let pattern = expr {
  line1;
  line2;
} else {
  line3;
  line4;
}

// above same as below but better

match expr {
  pattern => {
    line1;
    line2;
  }
  _ => {
    line3;
    line4;
  }
}

```

# `while Let`

```rust

while let pattern = expr {
  line1;
  line2;
  change(expr);
}

// above same as below but better

loop {
  match expr {
    pattern => {
      line1;
      line2;
      change(expr);
    }
    _ => break;
  }

}
```

