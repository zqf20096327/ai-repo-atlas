# CHANGELOG

## 2026-10-19 · 首次全量导出(v1.0 格式)

- A 层卡片 668 张(fn 字典序,九组字段,JSON Schema 校验通过)。
- 场景标签 v1.0:受控词表 47 标签/10 组(`data/vocab.json`),`links.scenario_tags` 为中文规范名;574 张卡带标签,其余为基建/学科类仓库的合法空。
- signals:maintenance/velocity 593 仓,downloads 278 仓;75 张新卡信号待下轮月更补齐(null 纪律)。
- 派生视图:`data/views/alternatives.jsonl`(1 个产品)。
- 格式说明:meta 不含 forks/open_issues(DATASET_PLAN §1);velocity 不含 domain_rank(域口径切换为词表组名,待 s9 月更重算)。

## 2026-11-17 · catalog 分片(v1.0.2 格式)

- 单文件 `data/catalog.jsonl` 于 11-02 涨破 GitHub 100MB 单文件硬限,此后每批推送被静默拒绝 4 天(11-06 发现停表)。
- 主表改为 8 分片 `data/catalog/part00..07.jsonl`(稳定分片键 `crc32(fn)%8`,每片 ~15MB,片内 fn 字典序)+ `MANIFEST.json`(片名/行数/字节/sha256)。
- 旧单文件已移除;全表读取 `cat data/catalog/part*.jsonl`(Shell 通配按片号序拼接,等价全表)。
