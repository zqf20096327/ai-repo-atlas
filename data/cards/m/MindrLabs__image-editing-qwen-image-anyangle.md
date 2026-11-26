# MindrLabs/image-editing-qwen-image-anyangle

⭐ 12 · MIT · 推送 2026-11-23 · [GitHub](https://github.com/MindrLabs/image-editing-qwen-image-anyangle) · 组织维护

**用 Qwen-Image 加 AnyAngle LoRA 按三维导向图改变照片视角的服务**

图像编辑服务：输入一张源照片和一张由三维模型渲染的粗略导向图，使用 Qwen-Image-2.1-Turbo 加 AnyAngle LoRA，按导向图的相机角度重绘源照片，通过 model-compose 运行，提供 Gradio 界面（端口 8097）与本地 API（端口 8096）。README 记录了在 RTX 4090、DGX Spark、Apple M2 上的运行实测（耗时、显存峰值、内存不足情况），并给出面部偏转角、人脸相似度、标签字符错误率等指标及各项声明的通过/未通过结论；无导向图时仅靠文本指令最多偏转约 14°。首次运行需下载约 32.5 GB 模型权重，无需 token。

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

- 按三维渲染导向图改变照片相机角度，人物可整圆转向
- 提供 Gradio 界面与 localhost API，可设置宽高与 seed
- 附 RTX 4090 与 DGX Spark 实测数据（单图 22.6–33 秒、显存峰值）
- 验证 AnyAngle LoRA 关闭时结果保持正面，说明其为角度跟随的必要组件

## 适用场景

- 把一张人物照片按指定角度重绘出多视角图像
- 产品照片按新相机角度重绘用于展示
- 在本地 NVIDIA GPU 上运行该图像编辑流程并复现实测结果

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L5: This service changes the camera angle of a photo with Qwen-Image-2.1-Turbo and the AnyAngle LoRA. It takes the sourc
> L7: Entering width, height, and seed in the gradio interface, uploading a source photo and a 60° guide, and getting the 
> L40: The API is at http://localhost:8096/api and the Gradio UI at http://localhost:8097. It takes two images, a source p


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `cb2c38809a07` · [字段定义](../../DATASET.md)*
