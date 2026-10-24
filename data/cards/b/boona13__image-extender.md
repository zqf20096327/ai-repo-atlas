# boona13/image-extender

⭐ 1,119 · TypeScript · MIT · 推送 2026-05-31 · [GitHub](https://github.com/boona13/image-extender) · [官网](https://github.com/boona13/image-extender) · 个人维护

**AI 图像外扩与 2D 游戏美术生成的开源 Web 应用**

基于 Next.js/TypeScript 的开源 Web 应用，通过 OpenRouter 调用 Google Gemini 图像模型做 outpainting（向四个方向扩展图像），并附带四个游戏美术工作区：多层视差背景、13 块 autotile 集生成、角色关键帧动画表、装饰道具库。关键机制包括泊松融合消除接缝、低频色漂移预校正、多候选择优、品红键抠像与视觉模型 QA/repaint 循环。BYOK 模式，API key 仅存于浏览器 localStorage。需自备 OpenRouter API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四方向 outpainting，每次扩展生成至多 3 个候选并按接缝质量排序供挑选
- 泊松融合（Pérez et al. 2003）+ 色漂移预校正消除原图与生成像素的接缝
- 五个工作区：Extender / 视差背景 / Autotile / 角色动画 / 装饰道具
- BYOK：OpenRouter key 仅存浏览器 localStorage，服务器不持久化

## 适用场景

- 把方图扩展成宽幅画面，接缝不可见
- 为 2D 平台游戏生成成套 autotile 与视差背景
- 生成跨帧身份一致的角色关键帧动画表
- 按文本提示从头生成图像再向外扩展

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L8: Powered by Google's Gemini image models via OpenRouter,
> L32: - **Extender** (default) — outpaint any image in any of four directions, with a

## 星数曲线

```mermaid
xychart-beta
    title "boona13/image-extender 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 1116 --> 1120
    line [1117, 1119, 1119]
```

2026-10-18 1,117 → 2026-10-24 1,119（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `5fa59dc72dd2` · [字段定义](../../DATASET.md)*
