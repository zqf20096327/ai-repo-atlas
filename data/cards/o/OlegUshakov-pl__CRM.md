# OlegUshakov-pl/CRM

⭐ 14 · HTML · MIT · 推送 2026-10-14 · [GitHub](https://github.com/OlegUshakov-pl/CRM) · 个人维护

**面向小型制造团队的本地 CRM/ERP，含 AI 助手**

基于 Django 6.x + HTMX + Tailwind 的自托管 CRM/ERP 平台，面向小型制造车间、CNC 工坊与工程事务所。核心为项目管理、任务、物料/BOM、工程文件（DXF/STEP/STL）、文档存储与知识库（文章/图库/文件三区）。AI 助手是其中一个模块：多供应商聊天（Ollama/Anthropic/OpenAI/DeepSeek 等 9 家）、命令模式通过正则意图识别执行 CRM 操作，含浏览器代理、网页搜索、AES-GCM 加密 API key 与写操作两步确认。通过 venv + pip 手动安装或 install.bat 一键部署，SQLite 存储，开发服务器仅绑 127.0.0.1，对外需配 WSGI 服务器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 项目/任务/物料 BOM/工程图纸（DXF、STEP、STL）统一管理
- 知识库分 Articles/Gallery/Files 三区，文章自动存为 .md 文件
- 多供应商 AI 助手：CHAT 与 COMMANDS 两种模式，支持 Ollama 本地模型
- 10 秒 AI 操作撤销、审计日志、SSRF/路径穿越防护

## 适用场景

- 小制造团队在一处管理项目、图纸、BOM 与文档
- 用自然语言命令让 AI 助手创建项目、添加任务、查联系人
- 本地/局域网部署，避免依赖大型企业级 ERP

## 场景标签

`AI 助手` `知识库管理` · 领域:对话与助手

## 证据(README 行号)

> L6: A lightweight CRM/ERP platform designed for engineering and manufacturing teams.
> L21: AI assistant for automation and team support
> L62: A project management, contractor and task tracking system featuring 17 custom apps, an AI assistant with a command 

## 星数曲线

```mermaid
xychart-beta
    title "OlegUshakov-pl/CRM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `deb947cb5fdc` · [字段定义](../../DATASET.md)*
