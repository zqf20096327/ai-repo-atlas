# judahpaul16/gpt-home

⭐ 653 · Python · GPL-3.0 · 推送 2026-09-13 · [GitHub](https://github.com/judahpaul16/gpt-home) · [官网](https://hub.docker.com/r/judahpaul/gpt-home) · 个人维护

**树莓派自制 AI 语音家庭助手，替代商业智能音箱**

面向 DIY 用户在 Raspberry Pi 上自建的家庭语音助手：通过 LiteLLM 接入 100+ LLM 提供商，用 LangGraph 构建 agent，提供天气、闹钟、提醒、日历、待办、翻译、音乐、灯光等用例，并集成 Spotify、Philips Hue、CalDAV、OpenWeatherMap 等服务。采用 Docker Compose 六服务架构（含 PostgreSQL+pgvector 持久记忆、NGINX、FastAPI 后端、React 前端），setup.sh 一键安装，最低支持 Pi Zero 2 W（512MB RAM）。限制：本地运行需自备 LLM API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LiteLLM 支持 100+ LLM 提供商，API key 可在 Web 界面设置
- 六服务 Docker Compose 架构，pgvector 持久记忆存储
- setup.sh 自动安装系统依赖并构建/拉取容器，可 --no-build 跳过构建
- 兼容多种开发板与系统（Pi 3B/4B/Zero 2W、Orange Pi、Ubuntu/Debian/Alma）

## 适用场景

- 用树莓派搭建自己的 AI 语音家庭助手
- 通过语音查询天气、设闹钟、管理日历和待办
- 联动 Spotify、Hue 灯光等已有家居服务

## 场景标签

`语音 Agent` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L9: ChatGPT at home! Basically a better Google Nest Hub or Amazon Alexa home assistant. Built on the Raspberry P iusing 
> L58: 2. ***Required:*** Set your API key. Copy the example config and add your key. GPT Home uses **LiteLLM** which supp
> L201: docker compose exec backend bash   # Voice assistant container

## 星数曲线

```mermaid
xychart-beta
    title "judahpaul16/gpt-home 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 652 --> 654
    line [653, 653]
```

2026-10-18 653 → 2026-10-25 653（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `6d5a2c12b49b` · [字段定义](../../DATASET.md)*
