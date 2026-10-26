# VaporTang/yolo-vision-pipeline-rknn

⭐ 49 · Python · Apache-2.0 · 推送 2026-07-28 · [GitHub](https://github.com/VaporTang/yolo-vision-pipeline-rknn) · 个人维护 · 中文 README

**面向瑞芯微 NPU 的 YOLOv8 训练-导出-转换一体化流水线**

将 YOLOv8 训练、ONNX 导出与 RKNN INT8 量化转换整合到单一代码库的部署工作流：Windows 侧负责训练与导出（setup_win.ps1 自动配置 conda 环境，使用瑞芯微定制版 YOLOv8 保证 NPU 兼容），Ubuntu/WSL 侧负责 RKNN 转换（校准数据集准备、INT8 量化）。附带数据集管理工具：视频抽帧、图像去重（含 GUI 人工审核）、训练/验证拆分与合并、类别过滤等，所有路径经 configs/paths.yaml 集中管理。面向需要在 RK3588/RK3568 等瑞芯微 NPU 上部署检测模型的开发者和嵌入式视觉工程师。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YOLOv8 → ONNX → RKNN 全流程整合于单一代码库与统一配置系统
- 支持 rk3588/rk3588s/rk3568/rk3566/rk3562 多平台转换
- 数据集工具链：抽帧、去重（含 GUI）、拆分/合并、校准集生成
- Win/WSL 分工明确：训练导出在 Windows，RKNN 转换需 x86_64 Linux

## 适用场景

- 把自训练的 YOLOv8 模型量化部署到 RK3588 板卡的 NPU
- 从录制的视频抽帧、清洗去重后构建训练数据集
- 用 X-Anylabeling 加载导出的 ONNX 模型做 AI 辅助标注

## 场景标签

`模型量化` `微调` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: **用于 YOLOv8 训练、导出并转换为 RKNN 格式以在瑞芯微 (Rockchip) NPU 上部署的统一工作流。**
> L12: 本项目将完整的 YOLOv8 → ONNX → RKNN 转换流程整合为一个结构清晰的单一代码库。它消除了以往分散在多个代码库中的繁杂工作流，并提供以下特性：
> L544: - **训练**：使用瑞芯微定制版的 YOLOv8 以确保 NPU 兼容性

## 星数曲线

```mermaid
xychart-beta
    title "VaporTang/yolo-vision-pipeline-rknn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-26 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `c76089755194` · [字段定义](../../DATASET.md)*
