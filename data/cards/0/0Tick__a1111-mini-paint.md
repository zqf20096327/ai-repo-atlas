# 0Tick/a1111-mini-paint

⭐ 123 · JavaScript · MIT · 推送 2026-02-14 · [GitHub](https://github.com/0Tick/a1111-mini-paint) · 个人维护

**stable-diffusion-webui 的 miniPaint 图像编辑器扩展**

面向 AUTOMATIC1111 stable-diffusion-webui 用户的浏览器扩展：集成 miniPaint 图像编辑器，支持将编辑后的图像发送到 Img2Img、ControlNet 与 Extras，也可从 txt2img、img2img、extras 通过 'Send to miniPaint' 按钮直接传入图像。安装走官方扩展索引（Extensions -> Available 搜索安装）；如需自定义 iframe 内功能，可进入 miniPaint 目录运行 npm run dev 或 npm run build 后重载界面。作者声明代码多汇编自其他免费扩展，允许自由取用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在 webui 内集成 miniPaint 图像编辑器
- 支持与 Img2Img、ControlNet、Extras 双向传送图像
- 通过官方扩展索引一键安装
- 可进入 miniPaint 目录用 npm run dev/build 自定义构建

## 适用场景

- 在 webui 内直接修图后送 Img2Img 或 ControlNet 生成
- 把 txt2img/img2img 产出的图像拉进编辑器继续处理

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L1: # AUTOMATIC1111 WebUI miniPaint extension
> L13: It provides the ability to send images to Img2Img, Controlnet and Extras.Send button

## 星数曲线

```mermaid
xychart-beta
    title "0Tick/a1111-mini-paint 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 122 --> 124
    line [123, 123]
```

2026-10-18 123 → 2026-10-25 123（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `b5a5315e911e` · [字段定义](../../DATASET.md)*
