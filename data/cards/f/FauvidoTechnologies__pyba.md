# FauvidoTechnologies/pyba

⭐ 31 · Python · MIT · 推送 2026-04-06 · [GitHub](https://github.com/FauvidoTechnologies/pyba) · [官网](https://pyba.readthedocs.io/) · 组织维护

**用自然语言驱动浏览器自动化的 OSINT 工具，可导出 Playwright 脚本**

PyBA 是面向 OSINT 的浏览器自动化软件：以 LLM 解析自然语言指令，自主导航任意网站执行任务（登录下载、社媒账号侦察、结构化数据抽取），并将成功会话导出为可独立运行的 Playwright Python 脚本，重复运行无需 AI 与 API 费用。提供 Normal/Step/DFS/BFS 四种探索模式，支持 OpenAI、VertexAI、Gemini 多提供商，凭据保存在环境变量中不暴露给 LLM。另含隐身反指纹、低内存模式、SQLite/PostgreSQL/MySQL 日志。目前处于 v0.3.0 活跃开发期，可能出现破坏性变更。

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

- 自然语言指令驱动 LLM 自主导航任意网站
- 成功运行可导出为独立 Playwright 脚本，重复运行无 AI 成本
- Normal/Step/DFS/BFS 四种探索模式
- Instagram/Gmail/Facebook 内置登录处理，凭据存于环境变量不暴露给 LLM

## 适用场景

- 让我用一句话让浏览器自动完成重复性任务（如下载银行账单）
- 做 OSINT 侦察：按用户名查找关联社媒账号、调研公司信息
- 把成功的自动化会话导出为脚本长期反复运行

## 场景标签

`浏览器自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L5:  PyBA uses LLMs to autonomously navigate any website, then exports the session as a standalone Playwright script - n
> L21: A browser automation software, specialized for OSINT purposes.

## 星数曲线

```mermaid
xychart-beta
    title "FauvidoTechnologies/pyba 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-28 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `08fc6ce2e2f8` · [字段定义](../../DATASET.md)*
