# sedum-dev/sedum

⭐ 14 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/sedum-dev/sedum) · [官网](https://sedum.dev) · 组织维护

**面向开发者的英文自然语言浏览器 e2e 测试 CLI**

构建在 Playwright 之上的开源测试工具（npm 包 sedum-cli）：测试中的每个 ai(...) 英文句子是一个步骤，由决策模型定位句子所指元素并判断断言是否在页面上成立，其余点击、输入、等待、判定均由 Playwright 确定性执行。默认决策模型为 TypeSafe Jev，可选用 Cloudflare Clef，两者返回概率而非自由文本；自带 API key 运行。支持 TypeScript 与 YAML 两种测试格式、并行与分片、JUnit 报告、CI 集成，并可生成供 Claude Code/Cursor 等 coding agent 修复失败的 markdown 报告。项目自述为 pre-alpha，Windows 为实验性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- ai(...) 英文句子步骤免选择器，步骤之间保留完整 Playwright/TypeScript 能力
- 决策模型返回概率并按阈值评分，边缘通过会被标记
- 支持 TypeScript 与 YAML 双格式测试，同一项目并行运行
- markdown 失败报告供 Claude Code/Cursor 等 coding agent 修复

## 适用场景

- 在每次 PR 上跑整套浏览器测试且控制成本
- 不维护选择器地编写登录、下单等端到端流程
- 让 coding agent 根据失败报告自动修复测试

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L28: Each `ai(...)` sentence is one step that Sedum resolves on the page, with no
> L33: Sedum uses a decision model for bounded tasks such as finding the element a
> L36: probabilities, not free text. Everything else is deterministic: clicking,

## 星数曲线

```mermaid
xychart-beta
    title "sedum-dev/sedum 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `64c87853ebe3` · [字段定义](../../DATASET.md)*
