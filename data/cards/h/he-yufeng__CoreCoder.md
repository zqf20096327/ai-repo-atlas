# he-yufeng/CoreCoder

⭐ 1,981 · Python · MIT · 推送 2026-11-27 · [GitHub](https://github.com/he-yufeng/CoreCoder) · [官网](https://pypi.org/project/corecoder/) · 个人维护 · 中文 README

**千行级可读的极简 AI 编码 agent，供学习与 fork**

以约 1,655 行引擎（全包 3,707 行 Python）实现的极简编码 agent，核心是包着大模型的 while 主循环加 8 个工具（bash、文件读写、glob、grep、todo、子 agent）。功能含 plan 模式、hooks、检查点、三级上下文压缩、模型回退链与 token/费用统计；修改磁盘或执行命令前需用户确认。默认走 OpenAI 兼容 API，可选 LiteLLM 后端。定位是可通读、可断点改跑的教学参考，作者明言不与生产级工具竞争用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 整个引擎可在一下午通读，支持任意行断点修改后重跑
- 8 个工具的完整 agent 循环，含子 agent 与三级上下文压缩
- 通过两个环境变量切换 OpenAI 兼容提供商，可选 LiteLLM 路由百余个
- plan 模式、Pre/PostToolUse hooks 与检查点机制

## 适用场景

- 想理解编码 agent 内部原理时逐行阅读源码
- 以它为基础 fork 出自己的 coding agent
- 用本地 Ollama 或 DeepSeek 等在终端跑一个最小 agent 循环

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L33: I've always felt coding agents get talked about as if they were arcane. Strip a tool like Claude Code or Cursor all
> L37: And it really runs: reads and writes files, executes shell, spawns sub-agents, compacts context in three tiers, and
> L60: Give it a model and a key and it goes. It speaks the OpenAI-compatible API by default, and switching providers is u

## 星数曲线

```mermaid
xychart-beta
    title "he-yufeng/CoreCoder 星数(近 24 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 1856 --> 1992
    line [1870, 1873, 1877, 1879, 1881, 1882, 1885, 1867, 1897, 1904, 1908, 1914, 1918, 1919, 1920, 1924, 1928, 1931, 1937, 1944, 1955, 1973, 1978, 1981]
```

2026-10-26 1,870 → 2026-11-28 1,981（+111）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `b5edd297aace` · [字段定义](../../DATASET.md)*
