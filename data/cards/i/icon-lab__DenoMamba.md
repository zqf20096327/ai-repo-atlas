# icon-lab/DenoMamba

⭐ 37 · Python · MIT · 推送 2025-11-05 · [GitHub](https://github.com/icon-lab/DenoMamba) · 组织维护

**低剂量CT去噪的融合状态空间模型官方PyTorch实现**

DenoMamba 的官方 PyTorch 实现，对应 arXiv:2409.13094 与 IEEE JBHI 论文。方法基于状态空间建模（SSM），采用沙漏型编码器-解码器结构：空间 SSM 模块编码空间上下文，通道 SSM 模块配合门控卷积网络编码通道上下文，特征经卷积融合模块（CFM）与低层输入特征合并。面向复现论文结果的科研用户：需自备配对的全剂量/四分之一剂量CT数据集，通过 train.py 训练、test.py 生成去噪图像。依赖 python>=3.8.13、torch>=2.2、cuda>=11.6。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 空间 SSM 与通道 SSM 双模块编码，卷积融合模块（CFM）合并特征
- 沙漏型编码器-解码器架构，捕获短程与长程上下文
- 提供 train.py/test.py 完整训练与测试命令及参数说明
- 需配对全剂量/四分之一剂量CT数据集（如LDCT目录结构）

## 适用场景

- 复现论文中的低剂量CT去噪结果
- 在自己的配对CT数据上训练与评估去噪模型
- 基于SSM架构开展医学图像去噪研究并二次开发

## 场景标签

`科研工具` `图像视频处理` · 领域:学习与行业

## 证据(README 行号)

> L4:  A fused state-space model for low-dose CT denoising
> L14: Official PyTorch implementation of **DenoMamba**, a novel denoising method based on state-space modeling (SSM), tha

## 星数曲线

```mermaid
xychart-beta
    title "icon-lab/DenoMamba 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-30 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `028470c0f24c` · [字段定义](../../DATASET.md)*
