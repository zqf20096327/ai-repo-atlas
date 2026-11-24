# kanaworksai-hue/kirapaint

⭐ 8 · Python · GPL-3.0 · 推送 2026-11-17 · [GitHub](https://github.com/kanaworksai-hue/kirapaint) · [官网](https://x.com/KanaWorks_AI) · 组织维护

**Blender 插件：把任意 3D 模型转为闪亮绘画风 2.5D**

免费开源（GPL-3.0-or-later）的 Blender 5.0+ 插件，面向想要手绘/绘画风渲染的 3D 创作者。工作流程为：在 Principled BSDF 前插入 KiraPaint Surface 着色器节点（沃罗诺伊面破碎法线、薄膜虹彩），配合彩色灯光与环境，再通过 KiraPaint Comp 合成器节点施加 bloom、两种各向异性 Kuwahara 滤镜与星光，输出笔触画面。不替换原材质，可一键还原；提供 4 种预设、10 种背景、动画切换与转台、日文本地化。渲染基于 EEVEE。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 表面破碎着色器 + 合成器笔触管线（Kuwahara×2、bloom、星光）
- 不替换原材质，Remove KiraPaint 一键还原
- 支持 glTF/FBX/OBJ/.blend，4 预设、10 背景、动画切换
- 提供 AGENTS.md，可由 Claude Code 等 AI agent 完成安装与调整

## 适用场景

- 把下载、扫描或 AI 生成的模型渲染成绘画风 2.5D
- 制作写实到绘画风过渡的动画展示
- 为 Blender 模型快速套用多种背景与风格的展示图

## 场景标签

 · 领域:3D 图形/创意工具

## 证据(README 行号)

> L18: **KiraPaint** は、Blender の 3D モデルを「キラキラの絵画風 2.5D」に変える、無料の Blender アドオンです。表面を小さなツヤのある面に砕いて、ピンク・水色・紫・金の光を映し込み、筆のタッチで塗り
> L20: ダウンロードしたモデル、スキャンしたモデル、AI で生成したモデルなど、**どんなモデルにも使えます**。元のマテリアルは置き換えず、前に処理を差し込むだけなので、いつでも元に戻せます。インストールから適用まで、AI エージェント
> L97: **必要なもの：** Blender 5.0 以降（Blender 5.1 と 5.2 で動作確認済み）、レンダーエンジンは EEVEE。

## 星数曲线

```mermaid
xychart-beta
    title "kanaworksai-hue/kirapaint 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-10", "2026-11-24"]
    y-axis "stars" 4 --> 9
    line [5, 8, 8]
```

2026-11-08 5 → 2026-11-24 8（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `75870eb0166b` · [字段定义](../../DATASET.md)*
