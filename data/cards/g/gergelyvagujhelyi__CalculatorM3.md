# gergelyvagujhelyi/CalculatorM3

⭐ 34 · Kotlin · GPL-3.0 · 推送 2026-06-29 · [GitHub](https://github.com/gergelyvagujhelyi/CalculatorM3) · 个人维护

**带离线 AI 手写数学求解器的 Android 计算器应用**

基于 Kotlin + Jetpack Compose 与 Material 3 的 Android 计算器，支持表达式求值、科学函数、历史记录、横屏与折叠屏适配，声明零数据收集、无广告无埋点。其中 AI 部分：拍摄手写数学表达式后由本地模型求解，全部推理在设备端完成，结果可插回计算器。模型通过 Google LiteRT-LM 运行，提供 Gemma 4/3n 四种视觉模型（2.6–4.9 GB），需 6–8 GB RAM；该功能默认隐藏，需连按 AC 七次解锁，且标注为实验性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 手写数学拍照后由设备端 AI 模型求解（实验性功能）
- 模型经 LiteRT-LM 本地运行，GPU 加速、CPU 自动回退
- Gemma 4/3n 四种模型可选，一次性下载 2.6–4.9 GB
- 零数据收集、零分析、无广告，无应用内相机权限

## 适用场景

- 日常科学计算并保留历史记录
- 拍下手写算式让本地 AI 给出解题步骤和答案
- 注重隐私、希望计算数据不出设备的用户

## 场景标签

`OCR` `多模态` · 领域:感知与多模态

## 证据(README 行号)

> L25: - **AI Math Solver** — photograph handwritten math and solve it on-device (experimental; hidden until you unlock it
> L41: 4. The model solves it entirely on-device — GPU-accelerated where supported — and streams its working, rendered wit
> L74: - AI models run entirely on-device — no cloud processing

## 星数曲线

```mermaid
xychart-beta
    title "gergelyvagujhelyi/CalculatorM3 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-26 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `05d4e151c2eb` · [字段定义](../../DATASET.md)*
