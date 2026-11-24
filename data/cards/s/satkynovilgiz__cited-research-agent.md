# satkynovilgiz/cited-research-agent

⭐ 3 · Python · 推送 2026-11-19 · [GitHub](https://github.com/satkynovilgiz/cited-research-agent) · 个人维护

**带强制来源引用的研究问答 agent：只引用实际抓取的页面**

基于 LangGraph 状态机与 Google Gemini 的命令行研究 agent：围绕一个研究问题逐步选择工具（DuckDuckGo 网页搜索、Wikipedia 搜索、页面抓取、LLM 摘要），每个下载页面成为可引用来源，答案中每个编号引用都经纯 Python 校验删除未实际抓取的编号。内置 8 次工具调用上限、失败重试与降级到 Wikipedia 搜索的回退逻辑，每步记录日志并保存 JSON 到 runs/ 目录，另提供 FastAPI Web API 和 run_agent Python 接口。需 Python 3.11+ 与 Gemini API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 引用编号必须对应实际下载的页面，伪造引用被自动删除
- 8 次工具调用步数上限，LangGraph recursion_limit 二重保护
- 搜索失败自动回退到 Wikipedia，逐条错误处理规则写明
- 每次运行的完整工具日志保存为 JSON 供评估

## 适用场景

- 生成带编号引用的研究问题回答
- 从 Python 代码中调用 run_agent 做批量评估
- 启动本地 Web API 供其他程序提问

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: An AI agent that answers a research question by **searching the web, reading pages, and citing its sources**.
> L26: 3. When it has enough evidence, or hits the **step limit (8 tool calls)**, it writes the answer using **only** the 
> L30: ## How it works (LangGraph)

## 星数曲线

```mermaid
xychart-beta
    title "satkynovilgiz/cited-research-agent 星数(近 2 点)"
    x-axis ["2026-11-22", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-22 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `44dffb656862` · [字段定义](../../DATASET.md)*
