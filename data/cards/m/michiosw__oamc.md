# michiosw/oamc

⭐ 14 · Python · MIT · 推送 2026-04-27 · [GitHub](https://github.com/michiosw/oamc) · 个人维护

**本地优先的 LLM 研究维基：原始资料编译为 Obsidian 知识库**

面向研究工作流的知识管理工具：将剪藏进 raw/ 的原始资料经固定管线编译为 wiki/ 下的 markdown 维基，以 Obsidian 作为主要阅读编辑界面。提供 Python CLI（llm-wiki），支持 ingest、query、lint、status、doctor、watch、process 等命令，附本地搜索/浏览/研究提示的 dashboard 与 macOS menubar 常驻运行时。vault 内容默认不进 git，保持本地。安装通过 uv，需配置 OPENAI_API_KEY。macOS 为推荐的日常运行平台。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- raw/ → wiki/ 的固定知识编译管线，raw/ 输入不可变
- llm-wiki CLI 覆盖 capture/process/query/lint/doctor/watch 工作流
- 本地 dashboard 与 macOS menubar 常驻运行时
- live vault 内容默认留在本地、被 git 忽略

## 适用场景

- 把剪藏的论文和资料整理成可查询的个人研究维基
- 在 Obsidian 中阅读和维护 LLM 生成的知识页面
- 用 query 命令对已有知识做综合提问

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L5: `oamc` is a local-first LLM wiki for research workflows.
> L69: uv run llm-wiki query "What does the wiki currently know about X?"

## 星数曲线

```mermaid
xychart-beta
    title "michiosw/oamc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `35a0156b0fca` · [字段定义](../../DATASET.md)*
