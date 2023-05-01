db.data.updateMany({}, [
  {
    $set: {
      ts: {
        $dateFromString: {
          dateString: "$ts",
          format: "%Y-%m-%d %H:%M:%S.%L",
          timezone: "-03:00"
        }
      }
    }
  }
])