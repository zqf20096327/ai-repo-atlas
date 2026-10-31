# qwe4559999/scopus-mcp

⭐ 48 · Python · MIT · 推送 2026-05-17 · [GitHub](https://github.com/qwe4559999/scopus-mcp) · 个人维护 · 中文 README

**让 Claude 等 MCP 客户端查询 Scopus 文献的服务器**

基于 Model Context Protocol 的服务器，封装 Elsevier Scopus API，向 AI 助手（如 Claude Desktop、Trae、Cursor）提供三个工具：search_scopus 按标准查询语法检索文献、get_abstract_details 按文档 ID 获取详情、get_author_profile 查作者档案。需先申请 Elsevier API key（通常要求机构订阅），通过 uvx 零配置运行或 pip 安装后以 Python 3.10+ 运行，密钥经 config.json 或环境变量配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 search_scopus / get_abstract_details / get_author_profile 三个 MCP 工具
- uvx 零配置接入 Claude Desktop，也支持 Trae 与 Cursor
- API key 经 config.json 或 SCOPUS_API_KEY 环境变量配置

## 适用场景

- 在 Claude Desktop 中用自然语言检索 Scopus 学术文献
- 让 AI 助手获取论文摘要详情与作者档案
- 在 Cursor/Trae 等 MCP 客户端中接入 Scopus 数据

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L7: This is a Model Context Protocol (MCP) server that provides access to the Elsevier Scopus API. It allows AI assistan
> L30: If you use Claude Desktop, you can skip downloading the code and just configure it directly:
> L63:  * **Command**: `uvx scopus-mcp`

## 星数曲线

```mermaid
xychart-beta
    title "qwe4559999/scopus-mcp 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29", "2026-10-31"]
    y-axis "stars" 45 --> 49
    line [46, 47, 48, 48]
```

2026-10-18 46 → 2026-10-31 48（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a9f7a92a74ba` · [字段定义](../../DATASET.md)*
