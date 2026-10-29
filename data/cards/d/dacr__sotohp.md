# dacr/sotohp

⭐ 44 · Scala · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/dacr/sotohp) · 个人维护

**面向海量家庭照片的 AI 管理与检索应用（人脸/物体检测）**

基于 Java 的照片管理软件，以 Docker 容器交付，提供 REST API 与 Web 界面：时间线浏览、幻灯片、世界地图查看、事件与人物管理、元数据编辑。照片目录保持只读，缩略图/人脸/物体检测结果缓存于本地，元数据存 LMDB，可选接入 Elasticsearch/OpenSearch 搜索。AI 能力包括人脸检测与批量识别（FaceInference 命令，欧氏距离匹配）、物体检测、图像分类与 AI 配图说明。定位为家庭网络私有使用，可选 Keycloak RBAC。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 人脸检测与批量识别、物体检测、图像分类、AI captioning
- 照片目录只读，缓存+LMDB 数据库，支持 15 万级照片规模
- Web UI + REST API + 时间线/地图/事件浏览，可选 Elasticsearch/OpenSearch 搜索
- Docker 交付，含预初始化演示容器

## 适用场景

- 家庭照片库的人脸识别与人物归类管理
- 在保持原目录结构不变的前提下管理和检索大量照片
- 按事件、时间线、地图浏览与编辑照片元数据

## 场景标签

`人脸识别` `目标检测` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L11: My favorite features are, of course, the diaporama, but also **people face identification**, **location fix**, **AI
> L44: - ⚠️ automated face recognition is still a batch process, done by this command FaceInference

## 星数曲线

```mermaid
xychart-beta
    title "dacr/sotohp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-29 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `16eb87c0f988` · [字段定义](../../DATASET.md)*
