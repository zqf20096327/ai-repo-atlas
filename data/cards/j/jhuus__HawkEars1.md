# jhuus/HawkEars1

⭐ 32 · Python · MIT · 推送 2026-03-11 · [GitHub](https://github.com/jhuus/HawkEars1) · 个人维护

**扫描录音识别鸟类鸣声并生成 Audacity 标签文件的桌面工具**

桌面程序，扫描音频录音检测鸟声并输出 Audacity 标签文件。内置针对加拿大及美国北部 334 种鸟类（另含 13 种两栖动物，测试有限）训练好的模型，基于 PyTorch 实现主模型集成加低频带模型（检测披肩榛鸡鼓翅）。可选安装 CUDA 或 Intel OpenVINO 加速推理，支持经纬度与日期参数降低误报。本仓库为 HawkEars 1.0，已被 HawkEars 2.0 取代，TensorFlow 旧版不再维护。模拟性鸟类（如嘲鸫）难以仅凭声音识别。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 扫描录音生成 Audacity 标签文件，覆盖 334 种鸟类
- PyTorch 模型集成 + 低频带模型检测披肩榛鸡鼓翅
- 可选 CUDA / Intel OpenVINO 加速推理
- 支持自训分类器与经纬度/日期过滤降低误报

## 适用场景

- 分析野外录音并生成可在 Audacity 中查看的物种标注
- 生态学研究中的鸟类声学监测与数据整理
- 训练自己区域的鸟类声音分类器

## 场景标签

 · 领域:生物声学/生态监测

## 证据(README 行号)

> L6: HawkEars is a desktop program that scans audio recordings for bird sounds and generates Audacity label files. It is 
> L88: HawkEars is implemented using PyTorch, with a primary model ensemble and a separate low-band model (data/low_band.c

## 星数曲线

```mermaid
xychart-beta
    title "jhuus/HawkEars1 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-31 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `abc4522da5a5` · [字段定义](../../DATASET.md)*
