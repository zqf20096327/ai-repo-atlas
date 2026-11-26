# brainlife/ezbids

⭐ 32 · Python · MIT · 推送 2026-11-25 · [GitHub](https://github.com/brainlife/ezbids) · [官网](https://brainlife.io/ezbids) · 组织维护

**神经科学数据到 BIDS 标准的转换工具，本地去标识**

ezBIDS 将神经生理（EEG/MEG/iEEG/NIRS/EMG）、神经影像（MRI/PET）与显微数据转换为 BIDS 标准结构。提供三种使用方式：brainlife.io 网页服务、Electron 桌面应用（beta，Mac 构建测试）与 aimport Python CLI。转换由启发式生成初猜结构，用户在界面中核对修改；本地模式数据不出机器，去标识（去脸、日期平移、标识符剥离），可选 AI agent 仅读取去标识后的纯文本，无 AI 时由内置启发式完成工作。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 三种使用方式：网页服务、Electron 桌面应用、aimport CLI
- 可选 AI agent 仅读取去标识后的纯文本，无 AI 时由内置启发式完成
- 去标识管线：去脸、标识符剥离、日期平移，输出须通过 BIDS v1.11.2 校验
- 支持 MRI/PET/多格式显微与电生理数据，含 Neuroglancer 等查看器

## 适用场景

- 将实验室扫描仪导出的 DICOM 转成 BIDS 数据集
- 上传 OpenNeuro 前对数据去标识并校验
- 院内敏感数据的本地化 BIDS 转换

## 场景标签

 · 领域:神经科学/科研数据处理

## 证据(README 行号)

> L3: The secure, semi-automated mapping of neuroscience data (neurophysiology, neuroimaging and microscopy) to the Brain 
> L17: check and the BIDS validator before anything can be uploaded, and you review every decision. The AI model is
> L41: Unlike other BIDS converters, ezBIDS eliminates the need for coding and command line interfaces (CLI), doing the bu


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `6c6c4c1fe149` · [字段定义](../../DATASET.md)*
