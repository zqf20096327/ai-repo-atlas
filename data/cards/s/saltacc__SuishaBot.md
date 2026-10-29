# saltacc/SuishaBot

⭐ 21 · Python · WTFPL · 推送 2026-09-07 · [GitHub](https://github.com/saltacc/SuishaBot) · 个人维护

**在 Discord 中运行 Stable Diffusion 生图的机器人**

Suisha 是一个 Discord 机器人，通过 Automatic1111 WebUI 的 API 作为后端运行 Stable Diffusion 生图。功能包括负向提示词、提示词权重、扩展 token 输入、VAE 支持、xformers、SD 1.x 与 2.x、highres fix。配置文件可大量定制，支持屏蔽词列表，可将任务队列拆分到多台机器的多个 GPU。权限与速率限制、img2img 尚在开发中。安装方式为 pip 安装依赖后运行 python main.py。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | WTFPL |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持负向提示词、提示词权重、VAE、xformers、SD 1.x/2.x、highres fix
- 队列可拆分到不同计算机/网络上的多个 GPU
- 通过 config.toml 与 .env 配置，含屏蔽词列表

## 适用场景

- 在 Discord 服务器里直接生图
- 利用多台机器的多 GPU 分摊生图队列
- 通过角色配置控制使用（开发中）

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L5: Suisha is a stable diffusion discord bot.
> L24: Suisha uses Automatic1111's WebUI as the backend.

## 星数曲线

```mermaid
xychart-beta
    title "saltacc/SuishaBot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e2f684a53830` · [字段定义](../../DATASET.md)*
