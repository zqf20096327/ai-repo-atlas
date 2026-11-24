# huynguyenvietwork/StackScout

⭐ 6 · Python · MIT · 推送 2026-11-20 · [GitHub](https://github.com/huynguyenvietwork/StackScout) · [官网](https://huynguyenvietwork.github.io/StackScout/) · 个人维护

**面向自托管开发者的每周技术雷达，结合个人技术栈对比新工具与 AI 模型**

自托管的每周技术雷达服务：采集约 60 个策展信息源（RSS、发布流、Hacker News、GitHub），AI 按固定分类法归类后与用户的技术栈匹配，为同类新技术生成带编号来源的对比页（基准、价格、优劣、切换成本），代码层强制每条声明附有效链接。默认仅监听 127.0.0.1、单本地用户无登录，以 Docker 镜像或 uv 从源码运行；AI 调用需 Anthropic API key 或 Claude Code CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每条对比声明强制附编号来源，无链接声明在代码层被丢弃
- 与用户技术栈同类别的新技术自动生成对比与 adopt/trial/watch/skip 结论
- 摘要投递支持 Telegram、Email、Slack、Discord 与 webhook，可定时调度
- 界面与 AI 产出支持 5 种语言

## 适用场景

- 每周追踪与我的技术栈同类的新工具和模型动态
- 评估是否要采用某个新框架/模型，看与我现有工具的对比
- 通过 Telegram 机器人随时生成和查询本周雷达

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: A weekly tech radar that reads the sources that matter, picks what is relevant to *the tools you actually use*, and 
> L15: > **Scope:** StackScout is currently designed for personal self-hosting. The web UI serves one local profile and ha
> L114: Enforced in code, not left to the AI:

## 星数曲线

```mermaid
xychart-beta
    title "huynguyenvietwork/StackScout 星数(近 2 点)"
    x-axis ["2026-11-21", "2026-11-24"]
    y-axis "stars" 5 --> 7
    line [6, 6]
```

2026-11-21 6 → 2026-11-24 6（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `975e8773c4b8` · [字段定义](../../DATASET.md)*
