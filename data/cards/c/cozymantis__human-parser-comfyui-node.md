# cozymantis/human-parser-comfyui-node

⭐ 139 · Python · GPL-3.0 · 推送 2026-04-13 · [GitHub](https://github.com/cozymantis/human-parser-comfyui-node) · [官网](https://cozymantis.gumroad.com) · 组织维护

**ComfyUI 人体解析节点：为身体部位与服装生成分割掩码**

CozyMantis 开发的 ComfyUI 自定义节点集，基于 Self-Correction for Human Parsing（SCHP）论文代码并改写支持 CPU 运行，对人体图像生成指定身体部位或服装单品的分割掩码。提供基于 LIP、ATR、Pascal Person Part 三个数据集训练的解析器，可识别的类别从帽子、上衣、裙子、裤子到头、躯干、四肢等；模型权重需从 Google Drive 手动下载到 models/schp 目录。安装方式为克隆仓库到 custom_nodes 后 pip 安装依赖；Windows 上编译 C++ 扩展需要 ninja、MSVC 等环境并附排障说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种解析器（LIP/ATR/Pascal），覆盖服装与身体部位共数十个类别
- 支持 CPU 和 CUDA 运行，VRAM 占用低
- 基于 SCHP（TPAMI 2020）方法更新而来

## 适用场景

- 为人物图像生成指定部位或服饰的掩码用于图像编辑
- 服装/时尚类图像分割（ATR 解析器面向 fashion AI）
- 虚拟试衣、换装工作流中的区域选择

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: Fast, VRAM-light ComfyUI nodes to generate masks for specific body parts and clothes or fashion items. Runs on CPU a
> L105: Based on the excellent paper "Self-Correction for Human Parsing" by Li, Peike and Xu, Yunqiu and Wei, Yunchao and 

## 星数曲线

```mermaid
xychart-beta
    title "cozymantis/human-parser-comfyui-node 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 137 --> 139
    line [138, 138]
```

2026-10-18 138 → 2026-10-25 138（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `788bbac61c70` · [字段定义](../../DATASET.md)*
