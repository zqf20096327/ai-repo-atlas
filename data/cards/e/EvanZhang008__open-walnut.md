# EvanZhang008/open-walnut

⭐ 37 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/EvanZhang008/open-walnut) · [官网](https://openwalnut.dev) · 个人维护

**自托管网页端管理本机与远程 Claude Code 会话的工作台**

自托管、本地优先的 Web 应用，用于在笔记本电脑和远程开发机上运行并监控 Claude Code：每台主机上的小型 daemon 持有 claude 进程，SSH 断开或笔记本休眠后会话继续运行，无需 tmux，daemon 由 SSH 自动部署。每个会话生成独立的文件 diff，可加行注释并回传评审。附带任务/项目管理、Markdown 笔记（wiki 链接）、长期记忆（BM25+本地向量检索）、Ask Walnut 个人 AI 代理、定时例程与插件系统。数据存储于 ~/.open-walnut/，无遥测。限制：需 macOS/Linux、Node 22+（npm 路线）及已登录的 Claude Code。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- daemon 持有 claude 进程，SSH 断开/浏览器关闭/服务器重启后会话继续运行
- 每会话独立 diff（基于会话历史重建而非 Git 状态），支持行注释评审回传
- 任务/笔记/记忆一体化，搜索结合 BM25 关键词、本地向量嵌入与新鲜度加权
- 首次启动自动下载本地嵌入模型 Qwen3-Embedding-0.6B（约 640 MB）

## 适用场景

- 在浏览器里并排运行和监控多个本机与远程 Claude Code 会话
- SSH 不稳定时保持远程开发机上的编码会话不中断
- 把任务规划、会话执行和变更评审集中在一个页面里管理
- 让 Ask Walnut 代理管理任务、写笔记并自动发起编码会话

## 场景标签

`编码 Agent` `Agent 记忆` `AI 助手` `知识库管理` · 领域:Agent 开发

## 证据(README 行号)

> L13: Open Walnut runs Claude Code on your laptop and on your remote dev boxes, and shows
> L14: every session in one web page. A small daemon on each host owns the `claude`
> L27: - **Claude Code workspace**: Run and monitor multiple Claude Code sessions side by side

## 星数曲线

```mermaid
xychart-beta
    title "EvanZhang008/open-walnut 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 33 --> 36
    line [34, 35, 35]
```

2026-10-18 34 → 2026-10-28 35（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9e1422540076` · [字段定义](../../DATASET.md)*
