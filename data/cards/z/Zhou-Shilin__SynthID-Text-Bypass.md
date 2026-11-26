# Zhou-Shilin/SynthID-Text-Bypass

⭐ 10 · Python · MIT · 推送 2026-08-16 · [GitHub](https://github.com/Zhou-Shilin/SynthID-Text-Bypass) · 个人维护

**研究演示：用 MLM 滑窗替换 token 擦除生成文本水印**

针对生成式文本水印（如 SynthID-Text）的擦除攻击研究演示：在每个 H token 滑动窗口内掩码并重填一个 token，由掩码语言模型（ModernBERT/mmBERT）补全，在保持语义的同时扰动水印统计特征。提供 Gradio 网页 UI、CLI 与 Python 库三种使用方式，按文本字符集自动选择模型，内置概率比、嵌入相似度等语义守卫参数，支持离线本地模型。README 声明仅限研究与教育用途，水印擦除可能违反服务条款或法律。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- H-token 滑窗单 token 掩码重填的最小编辑擦除算法
- Gradio UI 输出 token 级 diff、编辑表与守卫拒绝统计
- 支持 1800+ 语言的 mmBERT 与英文 ModernBERT，按脚本自动选择
- 可将 Hugging Face checkpoint 放入 models/ 实现完全离线运行

## 适用场景

- 研究水印算法在 token 编辑攻击下的鲁棒性
- 用开源统计水印检测器对比擦除前后检测 AUC
- 对多语言（CJK 等）生成文本做最小编辑实验

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: A research demo of a **scrubbing attack** against generative text watermarks
> L5: token is masked and re-filled by a masked language model (MLM), producing
> L122: ```python

## 星数曲线

```mermaid
xychart-beta
    title "Zhou-Shilin/SynthID-Text-Bypass 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-11-26"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-26 10 → 2026-11-26 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `b7931e82687f` · [字段定义](../../DATASET.md)*
