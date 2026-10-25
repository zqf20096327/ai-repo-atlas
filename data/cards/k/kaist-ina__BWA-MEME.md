# kaist-ina/BWA-MEME

⭐ 138 · C++ · MIT · 推送 2026-06-03 · [GitHub](https://github.com/kaist-ina/BWA-MEME) · [官网](https://ina.kaist.ac.kr/projects/bwa-meme/) · 组织维护

**用学习索引加速的 BWA-MEM2 等价 DNA 序列比对工具**

KAIST 团队开发的短读段序列比对工具：以学习索引（P-RMI）替代 FM-index 实现种子定位，端到端比对吞吐量较 BWA-MEM2 提升最高 1.4 倍，输出与 BWA-MEM2/bwa mem 0.7.17 相同的 SAM 文件，仅需在命令中加 -7 选项即可替换使用。面向 CPU-only 环境，无需专用硬件；索引内存 38GB 起步（全加速人类基因组 WGS 建议 140-192GB），提供 hg37/hg38 预训练模型下载。安装支持 Bioconda 或源码编译（需 libz、cmake）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 学习索引（P-RMI）种子定位，吞吐量较 BWA-MEM2 最高提升 3.32 倍
- 生成与 BWA-MEM2/bwa mem 0.7.17 相同的 SAM 输出，加 -7 选项即可替换
- CPU-only 运行，无需 GPU/FPGA 等专用硬件
- 提供 hg37/hg38 预训练 P-RMI 模型与索引下载

## 适用场景

- 在 CPU-only 服务器上运行人类基因组 WGS 比对
- 以低成本搭建高吞吐 NGS 比对集群
- 替换现有 BWA-MEM2 流程且保持 SAM 输出一致

## 场景标签

 · 领域:生物信息学/基因组学

## 证据(README 行号)

> L1: # BWA-MEME: BWA-MEM emulated with a machine learning approach
> L32: #### The seeding module of BWA-MEME uses Learned-index. This results in 3.32x higher seeding throughput compared to

## 星数曲线

```mermaid
xychart-beta
    title "kaist-ina/BWA-MEME 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 137 --> 139
    line [138, 138]
```

2026-10-18 138 → 2026-10-25 138（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `1d5a671c4eaa` · [字段定义](../../DATASET.md)*
