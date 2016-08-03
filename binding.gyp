
{
  "targets": [
    {
      "target_name": "pow",
      "include_dirs": [ "<!(node -e \"require('nan')\")" ],
      "sources": [ "pow.cpp" ]
    }
  ]
}