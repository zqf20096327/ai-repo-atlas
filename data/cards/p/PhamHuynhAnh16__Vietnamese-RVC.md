# PhamHuynhAnh16/Vietnamese-RVC

⭐ 35 · Python · MIT · 推送 2026-10-12 · [GitHub](https://github.com/PhamHuynhAnh16/Vietnamese-RVC) · 个人维护

**面向越南语用户的 RVC 语音转换工具：训练、转换与实时变声**

基于 RVC（Retrieval-based Voice Conversion）的语音转换工具，提供推理（人声分离、单/批量转换、语音识别结合转换、TTS、低延迟实时变声）、模型训练（含从 YouTube 自动构建训练数据）与扩展工具（多模型融合、ONNX/SVC 格式转换、F0 提取）。支持 30+ 种音高提取算法、20+ 嵌入模型、多种 vocoder 与 BF16/TF32/FP16/FP32/INT8 计算格式。作者声明项目偏实验性质、不保证稳定，无打包发行版，需手动安装或用 Colab/Kaggle 运行；界面支持越南语和英语。基于 Applio 与 RVC-WebUI 等项目构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- 推理/训练/扩展工具三组功能：人声分离、实时变声、TTS、批量转换
- 30+ 种音高提取算法（含混合模式）与 20+ 嵌入模型可选
- 支持 ONNX 导出与 BF16/TF32/FP16/FP32/INT8 计算格式
- 提供 Colab/Kaggle Notebook 与 Windows/Linux 安装脚本

## 适用场景

- 训练并转换自己的语音模型（含从 YouTube 自动构建数据集）
- 实时低延迟变声或批量处理音频文件
- 分离人声/伴奏后做歌声或语音转换

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L15: Dự án này là một công cụ chuyển đổi giọng nói. Với mục tiêu tạo ra các sản phẩm chuyển đổi giọng nói chất lượng cao
> L37: - Huấn Luyện Mô Hình: Tùy chỉnh các thông số kỹ thuật để huấn luyện ra mô hình giọng nói chất lượng nhất.

## 星数曲线

```mermaid
xychart-beta
    title "PhamHuynhAnh16/Vietnamese-RVC 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-30 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `cd0eb1560927` · [字段定义](../../DATASET.md)*
