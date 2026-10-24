# stevezau/shortlist

⭐ 104 · Python · MIT · 推送 2026-10-21 · [GitHub](https://github.com/stevezau/shortlist) · [官网](https://shortlistapp.dev/) · 个人维护

**给每个 Plex 用户生成私有推荐行的自托管工具**

自托管 Docker 服务：读取每个用户的 Plex 观看历史，从本地媒体库挑选未看过片目并生成该用户专属的推荐行（Picked for You、Because you watched、季节推荐等），通过 Plex 标签+共享过滤机制保证行仅对其所有者可见。推荐排名与理由由代码生成，无需 AI key；可选接入 Claude/GPT/Gemini 或本地模型（Ollama、llama.cpp 等）驱动 AI 网络搜索与文字描述行。仅支持 Plex，需 Plex Pass 与 PMS 1.43.2 以上，仅容器部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于每用户观看历史的私有推荐行，仅本人可见
- 排名与推荐理由由代码生成，无需 AI key
- 可选接入 Claude/GPT/Gemini 或本地模型（Ollama、vLLM 等）做 AI 搜索行
- 可选联动 Radarr/Sonarr、Overseerr 自动补库，支持干跑模式

## 适用场景

- 家庭 Plex 服务器上让每个成员看到个性化推荐行
- 配合现有 Radarr/Overseerr 栈自动补齐推荐片目
- 为节日和主题定制季节性推荐行

## 场景标签

`推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L14:  Shortlist is a free, open-source, self-hosted tool that gives each person on your
> L100: - 🧠 **Picks that exist, with no AI key needed.** Every pick is a title verified to be in your library,
> L102:  Gemini, or a local server such as Ollama, llama.cpp, LM Studio, vLLM or LocalAI) powers one extra

## 星数曲线

```mermaid
xychart-beta
    title "stevezau/shortlist 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 100 --> 105
    line [101, 104, 104]
```

2026-10-18 101 → 2026-10-24 104（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `9b0125e0810d` · [字段定义](../../DATASET.md)*
