# treeturtlefall-arch/FilmDateStamp

⭐ 3 · Python · MIT · 推送 2026-11-06 · [GitHub](https://github.com/treeturtlefall-arch/FilmDateStamp) · [官网](https://github.com/treeturtlefall-arch/FilmDateStamp) · 个人维护 · 中文 README

**ComfyUI 节点：模拟胶片石英日期印的物理光学烙印效果**

面向 ComfyUI 的自定义节点，用 7 阶段物理光学管线在图片上生成胶片相机石英日期戳：欧氏距离热点脊、多尺度 PSF 散射、H&D 光谱漂白、线性乳剂余量合成，并叠加 LED 抖动、压片板形变与银盐颗粒三类不规则性。内置 8 种字体（含 4 种自制硬件复刻 TrueType，OFL 1.1 授权）与 12 个年代/文化风格预设，输出 image/mask/date_text 三槽位。通过 ComfyUI-Manager、comfy-cli 或 git clone 安装，无需额外 pip 依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 阶段物理光学渲染管线（热点脊、PSF 散射、光谱漂白、乳剂余量合成）
- 8 种字体与 12 个风格预设，含字体视觉尺寸自动归一化
- 输出 emission mask，可接入下游 Film Grain 或 Inpaint 节点
- date_string 支持 auto/today/now 与种子可控的 vintage random

## 适用场景

- 给生成的或扫描的照片加上还原胶片相机日期戳效果
- 按年代/地区预设快速批量做复古风格后期
- 利用 mask 槽位对曝光区域追加颗粒或修补处理

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: ### Authentic Optical Burn-in & Emulsion Halation Engine for ComfyUI
> L123: ### Method 1: ComfyUI-Manager (Recommended)
> L141: 1. **Add the Node**: Right-click on the canvas → `image` → `film` → **`Film Date Stamp (Optical Burn-in)`**.

## 星数曲线

```mermaid
xychart-beta
    title "treeturtlefall-arch/FilmDateStamp 星数(近 2 点)"
    x-axis ["2026-11-10", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-10 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `0c19d47a3aec` · [字段定义](../../DATASET.md)*
