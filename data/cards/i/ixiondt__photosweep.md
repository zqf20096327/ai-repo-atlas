# ixiondt/photosweep

⭐ 3 · Python · AGPL-3.0 · 推送 2026-11-21 · [GitHub](https://github.com/ixiondt/photosweep) · 个人维护

**自托管 Nextcloud 照片库清理工具：本地视觉模型分类+感知哈希找重**

面向自托管 Nextcloud 用户：用本地运行的视觉模型（默认经 Ollama 调 qwen3-vl:8b）把每张图标记为截图、表情包、文档、废片、杂物、模糊或真实照片；另用 256 位感知哈希按内容找重复/相似照片，Same 组支持一键多选并删除前复核。删除经 Nextcloud WebDAV API 进入可恢复的 Deleted files，照片文件夹只读挂载，操作写入哈希链审计日志。以 Docker Compose 部署；无 GPU 时可经 OpenAI 兼容 API 转云端模型，需显式写入确认行。AGPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地视觉模型分类截图/表情包/文档/废片/杂物/模糊照片
- 256 位感知哈希按图像内容匹配重复与连拍相似组
- 删除经 WebDAV API 落入 Deleted files，附哈希链审计日志
- 云端模型路径需显式确认（PHOTOS_LEAVE_THIS_SERVER=yes）才会外发照片

## 适用场景

- 清理自托管 Nextcloud 里的截图与表情包堆积
- 找出 WhatsApp 转发、HEIC/JPEG 等重复照片
- 批量整理数万张家庭照片并保留可撤销的删除

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: Clean up a Nextcloud photo library with a vision model that runs on your own
> L18: - **Sorts the library.** A local vision model (default `qwen3-vl:8b` on
> L25:  files, same picture. They are matched by a 256-bit perceptual hash of the


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 mid · 依据 README sha `ab33ed97b8df` · [字段定义](../../DATASET.md)*
