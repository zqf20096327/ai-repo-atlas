# SedefVSR/SedefVSR

⭐ 3 · 推送 2026-11-26 · [GitHub](https://github.com/SedefVSR/SedefVSR) · [官网](https://sedefvsr.nuhyurdu.com) · 个人维护

**Windows 视频超分工具：扩散模型 4x 放大，本地 NVIDIA GPU 运行**

面向 Windows 的桌面视频超分辨率应用：用扩散模型把低分辨率素材放大 4 倍，全部计算在本地 NVIDIA GPU 上完成，素材不上传云端。提供渲染前的单帧对比预览、批量导出队列（进度/ETA/实时 fps）、暂停续跑（重启后可继续）、时间轴片段裁剪渲染。支持 H.265/H.264/AV1（NVENC 硬件编码）与多容器格式，亦可输出图片序列；VRAM 管理按显存自适应分块。要求 8 GB 以上显存与约 12 GB 磁盘空间。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 扩散模型 4x 超分辨率，带帧间时序一致性控制（防闪烁）
- 渲染前单帧 split 对比预览
- 导出队列支持暂停/续跑，重启后可恢复
- NVENC 硬件编码，支持 HEVC/H.264/AV1 与多格式

## 适用场景

- 把旧低清视频在本地放大到高清
- 批量导出多个待放大视频文件
- 只渲染时间轴上选定的片段

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: AI video upscaler for Windows. Turns old or low-resolution footage into sharp
> L11: - **4× upscaling** — diffusion super-resolution tuned for consumer NVIDIA GPUs
> L25: |**GPU**|NVIDIA with 8 GB VRAM or more|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `1e3d1ea92e91` · [字段定义](../../DATASET.md)*
