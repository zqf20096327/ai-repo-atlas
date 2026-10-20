# CHANGELOG

## 2026-10-19 · 首次全量导出(v1.0 格式)

- A 层卡片 666 张(fn 字典序,九组字段,JSON Schema 校验通过)。
- 场景标签 v1.0:受控词表 47 标签/10 组(`data/vocab.json`),`links.scenario_tags` 为中文规范名;573 张卡带标签,其余为基建/学科类仓库的合法空。
- signals:maintenance/velocity 593 仓,downloads 278 仓;73 张新卡信号待下轮月更补齐(null 纪律)。
- 派生视图:`data/views/alternatives.jsonl`(1 个产品)。
- 格式说明:meta 不含 forks/open_issues(DATASET_PLAN §1);velocity 不含 domain_rank(域口径切换为词表组名,待 s9 月更重算)。
