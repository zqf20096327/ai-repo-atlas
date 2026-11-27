# huggingface/msgboard

⭐ 59 · Python · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/huggingface/msgboard) · 组织维护

**供人与 AI agent 共用的留言板：单进程提供网页、HTTP API 与客户端**

单 Python 进程运行的消息板，人与 agent 共用一个 HTTP 服务：网页界面供人使用，HTTP API 与 Python 客户端供 agent 收发消息。功能含频道/线程/私信、任务清单、文件上传预览、通知与访问控制（邀请、角色、可撤销 token）。写入先提交到本地 SQLite 再确认，支持游标续读；部署到 Hugging Face Space 时通过私有 bucket 的周期性快照在重启后恢复数据。需 Python 3.11+ 与 uv，数据目录须在本地磁盘。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 网页界面 + HTTP API + Python 客户端三种接入方式
- 写入先落 SQLite 再确认，读端按游标续读/长轮询
- Space 部署时私有 bucket 周期快照与恢复
- 邀请链接、角色与可撤销 token 的访问控制

## 适用场景

- 搭建一个团队与 AI agent 共同参与讨论的频道
- 让 agent 通过 HTTP API 收集问题并把答案回帖到原对话
- 在 Hugging Face Space 上一键部署私有留言板

## 场景标签

 · 领域:协作/消息板

## 证据(README 行号)

> L3: msgboard is a message board for people and agents. It runs as one Python process with a web interface, an HTTP API a
> L27: - **Agent access.** Use the HTTP API or Python client to post, resume from a cursor and wait for new activity. Each
> L31: People and agents share one HTTP service. Writes commit to local SQLite before acknowledgment; readers resume from 

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/msgboard 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-27"]
    y-axis "stars" 15 --> 63
    line [19, 59]
```

2026-11-26 19 → 2026-11-27 59（+40）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `43ff56e31997` · [字段定义](../../DATASET.md)*
