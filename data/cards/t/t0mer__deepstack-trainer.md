# t0mer/deepstack-trainer

⭐ 26 · Python · GPL-3.0 · 推送 2026-09-28 · [GitHub](https://github.com/t0mer/deepstack-trainer) · 个人维护

**给自托管用户的 DeepStack 人脸训练与测试 Web 界面**

基于 FastAPI 的 Web 应用，用于训练和测试 DeepStack AI 服务器：上传照片与姓名注册人脸，测试人脸识别、物体检测与场景识别，并提供照片画廊与最低置信度配置。面向使用 DeepStack 做家庭自动化（如 Home Assistant、Blue Iris）的自托管用户。照片存于 photos/uploads，元数据写入 SQLite；自身无认证，需运行于可信网络；浏览器加载 CDN 与 Google Analytics。以多架构 Docker 镜像分发，也可从源码构建或 pip 安装依赖后本地运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 浏览器内完成人脸注册、识别、物体检测与场景识别测试，无需手写 API 调用
- 照片画廊支持重命名与删除（仅改动 trainer 自身数据库）
- 多架构 Docker 镜像（amd64/arm64/arm/v7）
- 支持 DeepStack API key 与可配置最低置信度

## 适用场景

- 给自托管的 DeepStack 服务器录入家庭成员人脸
- 在浏览器中测试 DeepStack 的识别与检测效果
- 管理和浏览已注册的人脸照片画廊

## 场景标签

`人脸识别` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L10: DeepStack Trainer is a FastAPI-powered web application that makes it as easy as possible to train and test a DeepSt
> L12: It is aimed at self-hosters who run DeepStack for home automation (for example with Home Assistant or Blue Iris) an

## 星数曲线

```mermaid
xychart-beta
    title "t0mer/deepstack-trainer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-26 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `753d3587e138` · [字段定义](../../DATASET.md)*
