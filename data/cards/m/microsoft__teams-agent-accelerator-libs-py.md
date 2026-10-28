# microsoft/teams-agent-accelerator-libs-py

⭐ 28 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/microsoft/teams-agent-accelerator-libs-py) · 组织维护

**微软 Teams 个人 agent 开发库（Python，带记忆服务集成）**

微软维护的 Python 库，用于在 Teams 上开发 pro-code 的个人 agent，集成记忆服务（memory service）。仓库提供基于 uv 的开发环境搭建流程（uv sync 安装虚拟环境与依赖，Windows 可能需手动安装 cargo），支持通过 .env 配置 Azure OpenAI 的 API key、部署名（gpt-4o、text-embedding-3-small）与 API 地址用于测试调试，可用 pytest 运行记忆模块等测试用例，另带 test bot 运行方式（见 src/README.md）。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 面向 Teams 的 pro-code 个人 agent 开发库
- 集成记忆服务（memory module，含专项测试）
- 通过 .env 配置 Azure OpenAI 模型进行调试
- 基于 uv 的环境与依赖管理

## 适用场景

- 在 Teams 中开发带记忆能力的个人 agent
- 接入 Azure OpenAI 的 gpt-4o 与 embedding 模型进行调试测试
- 基于该库运行测试 bot 验证 agent 行为

## 场景标签

`Agent 框架` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L1: # Teams Agent Accelerator - Python
> L60: Mac: `pytest tests/test_memory_module.py`

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/teams-agent-accelerator-libs-py 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `cb4ec6ade0a3` · [字段定义](../../DATASET.md)*
