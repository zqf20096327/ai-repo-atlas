# ronibandini/AdversarialPatternsLab

⭐ 3 · Python · GPL-3.0 · 推送 2026-10-22 · [GitHub](https://github.com/ronibandini/AdversarialPatternsLab) · 个人维护

**本地生成对抗图案并测试 Edge Impulse 检测器的工具**

该工具生成 36 种程序化种子图案，通过透明 PNG 服装掩膜合成到人物照片上，再交由本地运行的 Edge Impulse `.eim` 检测模型评估：记录目标标签的置信度并与阈值比较，输出带边界框的结果图、结果表、日志与按图案的检出率，并可导出成功图案的 zip（含合成图、测试补丁、1200px 补丁与 CSV）。运行需 Linux/WSSL2、Python 3.9+ 与针对本机 CPU 架构导出的 `.eim` 模型，面向做对抗补丁实验的安全研究者与创客。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 36 种程序化种子图案，分 7 组（几何、自然纹理、物体形状、迷彩等）
- 基于掩膜的图案合成，保留照片原阴影
- 本地 `.eim` 模型逐图案评估，记录目标标签置信度与检出率
- 导出成功图案 zip 与 CSV 结果

## 适用场景

- 测试自训 Edge Impulse 人员检测模型对图案干扰的响应
- 为物理对抗补丁研究批量生成并筛选候选图案
- 隐私场景下评估检测系统对服装图案的置信度变化

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: Generate patterns, apply them to a person's clothing through a mask, and measure how a **local** Edge Impulse (`.eim
> L13: 3. **Evaluates on a local model.** Each variant goes through your `.eim` model. The tool records the confidence for

## 星数曲线

```mermaid
xychart-beta
    title "ronibandini/AdversarialPatternsLab 星数(近 2 点)"
    x-axis ["2026-11-10", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-10 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `9781db28a2a0` · [字段定义](../../DATASET.md)*
