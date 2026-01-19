def dict_to_table(data: dict, col1="Key", col2="Value") -> str:
    rows = "".join(
        f"<tr><td>{k}</td><td>{v}</td></tr>"
        for k, v in data.items()
    )
    return f"""
      <table>
        <thead>
          <tr>
            <th>{col1}</th>
            <th>{col2}</th>
          </tr>
        </thead>
        <tbody>
          {rows}
        </tbody>
      </table>
    """
