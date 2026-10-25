# hoangsonww/Moodify-Emotion-Music-App

⭐ 82 · JavaScript · MIT · 推送 2026-09-27 · [GitHub](https://github.com/hoangsonww/Moodify-Emotion-Music-App) · [官网](https://moodify-app.vercel.app) · 个人维护

**基于情绪检测的音乐推荐应用：分析文本/语音/表情推荐音乐**

全栈情绪音乐推荐系统：用三个自训练 AI/ML 模型检测文本、语音与面部表情的情绪，据此推荐音乐，推荐曲目经 Deezer 免费网页播放器打开。前端 React，后端 Django/FastAPI，ML 推理运行在 Modal（scale-to-zero，空闲后首次请求约 1-2 秒，模型失败返回中性兜底）。含 Thompson-Sampling 上下文 bandit 的逐用户在线强化学习重排序、WebAuthn 免密登录、PWA 与移动端（React Native/Expo）。仓库提供 Makefile 单命令入口及 Kubernetes/Terraform/Helm 等自托管配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文本/语音/面部三种情绪检测模型，实时输出音乐推荐
- 逐用户 Thompson-Sampling bandit 在线重排序（👍/👎/打开 Deezer 反馈）
- WebAuthn/FIDO2 免密登录，支持多设备 passkey 与无用户名登录
- Kubernetes/Terraform/Helm/Argo CD 自托管配置与 Docker 支持

## 适用场景

- 根据我当前的情绪获得音乐推荐
- 通过打字、说话或面部表情检测情绪
- 对推荐曲目投票以逐步个性化播放列表

## 场景标签

`推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L10: The **Moodify** project is an integrated emotion-based music recommendation system that combines frontend, backend,
> L12: Supporting both desktop and mobile platforms, **Moodify** offers a seamless user experience with real-time emotion 
> L202: - 🎯 **Online reinforcement learning** — every user trains their own playlist ranker in real time. A "Was this righ

## 星数曲线

```mermaid
xychart-beta
    title "hoangsonww/Moodify-Emotion-Music-App 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 81 --> 83
    line [82, 82]
```

2026-10-18 82 → 2026-10-25 82（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `72a54b1c4683` · [字段定义](../../DATASET.md)*
