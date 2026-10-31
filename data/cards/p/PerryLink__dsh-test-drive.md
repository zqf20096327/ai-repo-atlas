# PerryLink/dsh-test-drive

⭐ 13 · TypeScript · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/PerryLink/dsh-test-drive) · [官网](https://perrylink.github.io/plugins/dsh-test-drive/) · 个人维护 · 中文 README

**DSH 插件的隔离安装冒烟测试工具，输出 pass/fail 结果矩阵**

面向 DeepSeek Harness 插件开发者的测试插件：在一次性 DSH_HOME profile 中执行完整流水线——安装（git/npm/本地包/tarball）、--dump-config 补丁校验、无头启动冒烟、可选能力断言、卸载与隔离区清理——真实 ~/.dsh 不被触碰。每个阶段产生结构化记录（schema dsh-test-drive/v1），批量运行以 /testdrive 后台任务生成 JSON+Markdown 矩阵，供 dsh-score 等下游评分管线消费。附带 GitHub Actions composite action，输出 PR 评论与 JUnit XML；能力断言阶段需要 DEEPSEEK_API_KEY，缺失时标记 skipped 而非 fail。限制：不支持 DSH Desktop 作为测试宿主，需可二次无头启动的 dsh CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- install→patch check→boot smoke→capability→uninstall→cleanup 完整流水线，宿主 profile 不被读写
- 结构化结果 schema dsh-test-drive/v1，含各阶段状态、时长与整体 verdict（pass/fail/partial/unknown）
- 附带 GitHub Actions composite action，输出 Markdown 与 JUnit XML
- 临时目录前缀注册与 dry-run→隔离改名→删除清理梯，报告经凭据脱敏

## 适用场景

- 插件发布前在隔离环境跑安装与冒烟验证
- 批量测试候选插件并生成 pass/fail 矩阵供选型评分
- 在 CI 的 PR 中自动展示插件测试结果

## 场景标签

 · 领域:开发者工具/AI agent 插件测试

## 证据(README 行号)

> L7: **Isolated install-and-smoke test drives for DeepSeek Harness plugins.**
> L64: - `test_drive` tool — one target through the complete pipeline: `dsh plugin add` → `--dump-config` patch check → he
> L68: - Structured results — every record carries the discriminator `schema: "dsh-test-drive/v1"` with first-class fields

## 星数曲线

```mermaid
xychart-beta
    title "PerryLink/dsh-test-drive 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `3be7a0ac64be` · [字段定义](../../DATASET.md)*
