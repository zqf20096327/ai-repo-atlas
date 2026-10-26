# haseeb-heaven/gworkspace-agent

⭐ 82 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/haseeb-heaven/gworkspace-agent) · 个人维护

**自然语言操作 Google Workspace 的自主 AI Agent**

基于 LangChain ReAct + LangGraph DAG 混合架构的自主 agent，把自然语言转为跨 Gmail、Drive、Sheets、Docs、Calendar 等 20+ Google 服务、100+ 动作的多步工作流。LLM 规划器生成任务 DAG，执行采用 Reason→Act→Observe 循环；内置 5 步验证引擎、默认只读模式、E2B 沙箱代码执行与 Mem0 长期记忆，支持 OpenAI/Anthropic/OpenRouter 模型回退链。提供 CLI、桌面 GUI、Gradio Web 与 Telegram 四种界面，源码安装 pip install -e . 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 20+ Google 服务、100+ 动作的多服务编排
- 5 步不可绕过验证引擎（参数/权限/结果/完整性/幂等）
- 模型注册表与 OpenAI/Anthropic/OpenRouter 自动回退
- 默认只读模式、E2B 沙箱代码执行与收件人锁定等安全机制

## 适用场景

- 用一句话完成邮件筛选、附件归档并生成表格日志
- 跨服务链式任务：读邮件提取待办写入 Tasks 并建日程提醒
- 在沙箱中运行 Python 处理 Drive 上的数据文件

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L11: An autonomous AI agent for Google Workspace, built on a hybrid **LangChain ReAct + LangGraph DAG** architecture. It
> L131: gws_cli --task "List my drive files"

## 星数曲线

```mermaid
xychart-beta
    title "haseeb-heaven/gworkspace-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 81 --> 83
    line [82, 82]
```

2026-10-18 82 → 2026-10-26 82（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `655865f14b67` · [字段定义](../../DATASET.md)*
