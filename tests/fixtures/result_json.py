json_nested_result = '''{
  "common": {
    "type": "nested",
    "value": {
      "follow": {
        "type": "added",
        "value": false
      },
      "setting1": {
        "type": "not_changed",
        "value": "Value 1"
      },
      "setting2": {
        "type": "removed",
        "value": 200
      },
      "setting3": {
        "new_value": null,
        "old_value": true,
        "type": "changed"
      },
      "setting4": {
        "type": "added",
        "value": "blah blah"
      },
      "setting5": {
        "type": "added",
        "value": {
          "key5": "value5"
        }
      },
      "setting6": {
        "type": "nested",
        "value": {
          "doge": {
            "type": "nested",
            "value": {
              "wow": {
                "new_value": "so much",
                "old_value": "",
                "type": "changed"
              }
            }
          },
          "key": {
            "type": "not_changed",
            "value": "value"
          },
          "ops": {
            "type": "added",
            "value": "vops"
          }
        }
      }
    }
  },
  "group1": {
    "type": "nested",
    "value": {
      "baz": {
        "new_value": "bars",
        "old_value": "bas",
        "type": "changed"
      },
      "foo": {
        "type": "not_changed",
        "value": "bar"
      },
      "nest": {
        "new_value": "str",
        "old_value": {
          "key": "value"
        },
        "type": "changed"
      }
    }
  },
  "group2": {
    "type": "removed",
    "value": {
      "abc": 12345,
      "deep": {
        "id": 45
      }
    }
  },
  "group3": {
    "type": "added",
    "value": {
      "deep": {
        "id": {
          "number": 45
        }
      },
      "fee": 100500
    }
  }
}'''