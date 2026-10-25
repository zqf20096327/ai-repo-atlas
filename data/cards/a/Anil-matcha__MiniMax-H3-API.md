# Anil-matcha/MiniMax-H3-API

⭐ 55 · Python · MIT · 推送 2026-10-01 · [GitHub](https://github.com/Anil-matcha/MiniMax-H3-API) · [官网](https://muapi.ai/minimax-h3) · 个人维护

**MiniMax H3 视频生成 API 的 Python SDK**

面向 MiniMax Hailuo H3 模型（经 MuAPI 平台访问）的 Python 客户端 SDK，覆盖文生视频、图生视频、参考素材生视频与首尾帧引导等工作流。基于 requests 构建，提供提交任务、轮询结果、webhook 的异步接口；需要设置 MUAPI_API_KEY 环境变量。支持 pip 安装或源码安装，要求 Python 3.9+，MIT 许可。

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

- 文生视频/图生视频/参考生视频/首尾帧引导四种工作流
- 提交-轮询-webhook 异步任务接口
- 首尾帧旧接口 first_last_frame() 兼容别名映射到 image_to_video()

## 适用场景

- 在 Python 应用中接入 MiniMax H3 的视频生成
- 用首尾帧图片控制视频起止画面
- 通过参考图片/视频素材生成产品展示视频

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L7: Python SDK for the **MiniMax H3 API** on Muapi. Generate video from text, animate a still image, or guide a new vide
> L37: pip install minimax-h3-api

## 星数曲线

```mermaid
xychart-beta
    title "Anil-matcha/MiniMax-H3-API 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-25"]
    y-axis "stars" 52 --> 56
    line [53, 54, 55, 55]
```

2026-10-18 53 → 2026-10-25 55（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `fa560d14187d` · [字段定义](../../DATASET.md)*
