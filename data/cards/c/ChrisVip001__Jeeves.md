# ChrisVip001/Jeeves

⭐ 53 · Rust · MIT · 推送 2026-11-22 · [GitHub](https://github.com/ChrisVip001/Jeeves) · [官网](https://github.com/ChrisVip001/Jeeves/releases) · 个人维护 · 中文 README

**本地运行的的个人任务助理 Agent，记忆可审计**

运行在用户自己机器上的个人助理：规划并执行多步任务，逐步骤写入 append-only 账本（记录检索决策、工具调用、所用模型与成本），记忆库通过 ledger 链接回溯源，FTS5 索引可重建。Rust 实现核心代理循环、记忆与 21 个内置工具（含沙箱命令、文件读写、定时任务、子代理委派），TypeScript 实现聊天网关（WeChat/Lark）与浏览器适配器。支持 12 家 LLM 提供商，无 API key 时可用 Ollama 离线运行。提供 Mac 应用、Docker 与源码三种安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每轮对话写入 append-only 账本，记忆与决策可逐条检查
- 21 个内置工具（13 常开、8 需开关）+ MCP 服务器扩展
- 12 家 LLM 提供商预适配，Ollama 可离线使用
- 确定性回放评测与 judge 评分把关每次发布

## 适用场景

- 在本机运行个人助理，处理多步骤任务且保留完整执行痕迹
- 需要检查助理每步调用了哪些工具、花费多少的隐私敏感用户
- 通过微信或飞书与本地助理对话并调用飞书业务能力

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L9: **A personal assistant that runs on your own machine, with a memory you can inspect.**
> L10: It plans, executes, recovers, verifies and delivers multi-step personal tasks; everyday conversation is supporting 

## 星数曲线

```mermaid
xychart-beta
    title "ChrisVip001/Jeeves 星数(近 4 点)"
    x-axis ["2026-11-19", "2026-11-21", "2026-11-22", "2026-11-23"]
    y-axis "stars" 45 --> 118
    line [112, 94, 51, 53]
```

2026-11-19 112 → 2026-11-23 53（-59）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `ff991d434629` · [字段定义](../../DATASET.md)*
