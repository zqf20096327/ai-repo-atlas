# feicaiclub/deepseek-harness-whitepaper

⭐ 13 · HTML · MIT · 推送 2026-08-15 · [GitHub](https://github.com/feicaiclub/deepseek-harness-whitepaper) · [官网](https://feicaiclub.github.io/deepseek-harness-whitepaper/) · 组织维护 · 中文 README

**DeepSeek Harness（dsh）131 页白皮书：安装、源码解析到插件扩展教程**

由废才俱乐部独立编写的 131 页中文白皮书，讲解 DeepSeek 于 2026 年 8 月以 MIT 协议开源的 agent harness `dsh`。全书七部三十八章，覆盖安装、配模型、219 个包的组成、一次对话的完整流程、插件编写与扩展点。所有代码行为判断回仓库源码核对，实测数字包括 52 个内置工具、26 条能力接缝等，并记录遥测端点硬编码、Web 无鉴权等代价项。提供 PDF 下载与在线阅读，可用 git clone 起本地服务。研究基线为 0.1.0-rc.5，注明项目快速迭代中文档会过时。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 131 页七部三十八章，所有结论回源码核对
- 记录实测数字：219 个包、52 个内置工具、26 条能力接缝、44 种会话事件
- 含完整可跑的工具插件代码示例
- 按读者类型（使用者/插件作者/选型者）给出三条阅读路线

## 适用场景

- 深入研究 dsh 的架构与「一切皆插件」主张
- 照着做装、配模型、接 CI、写第一个插件
- 做 agent harness 选型前了解 dsh 的代价与风险项

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L7: 131 页 · 七部三十八章 · 全部结论回源码核对
> L20: 这份白皮书把它拆开讲清楚。131 页，从「harness 到底是什么」讲到「你自己写的插件怎么装进去」。
> L93: - 研究基线：`deepseek-harness` **0.1.0-rc.5**（仓库源码版本；npm 上 `latest` 标签当时是 `0.1.0-rc.6`，两者不是一回事，书中凡涉及都说明了是哪一个）

## 星数曲线

```mermaid
xychart-beta
    title "feicaiclub/deepseek-harness-whitepaper 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `a948f7a37a3f` · [字段定义](../../DATASET.md)*
