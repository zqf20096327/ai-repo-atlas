# Guillain-RDCDE/FLAC_Detective

⭐ 26 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/Guillain-RDCDE/FLAC_Detective) · [官网](https://pypi.org/project/flac-detective/) · 个人维护

**检测伪装成 FLAC 的有损压缩音乐文件的工具**

面向音乐收藏者的命令行工具：扫描 FLAC 文件库，识别由 MP3、AAC（含 HE-AAC v2）、Vorbis、Opus 转码伪装成无损的文件。综合三类独立证据——频谱分析、编码器残留算术特征、训练模型——需至少两类证据一致才给出定罪，定罪输出为四档红绿灯式结论（AUTHENTIC/WARNING/SUSPICIOUS/FAKE_CERTAIN）。设计取向为校准检测：宁可漏检也不误判。扫描只读不改文件。pip 安装，需 Python 3.10+。

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

- 检测 MP3/AAC/Vorbis/Opus 伪装成 FLAC 的有损转码
- 三类独立证据（频谱、编码器算术、训练模型）需至少两类一致才定罪
- 四档结论输出：AUTHENTIC/WARNING/SUSPICIOUS/FAKE_CERTAIN
- 只读扫描，不修改任何文件

## 适用场景

- 核查购买的无损音乐是否为有损转码
- 批量扫描整个音乐库找出可疑文件
- 购买二手或来源不明的 FLAC 前做真伪检验

## 场景标签

 · 领域:音频分析/应用机器学习

## 证据(README 行号)

> L7: > Independent kinds of evidence, spectral analysis, encoder arithmetic and a trained model; a verdict needs agreemen
> L13: > MP3, AAC (HE-AAC v2 included), Vorbis and Opus, through independent kinds of evidence. A conviction needs two of 
> L23: A lossy codec throws away the top of the spectrum and never gives it back. FLAC Detective reads

## 星数曲线

```mermaid
xychart-beta
    title "Guillain-RDCDE/FLAC_Detective 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 27
    line [25, 26]
```

2026-10-18 25 → 2026-10-29 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `848aaecd3516` · [字段定义](../../DATASET.md)*
