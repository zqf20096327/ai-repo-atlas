# Mactarvish/vue-image-viewer

⭐ 43 · Vue · 推送 2026-10-26 · [GitHub](https://github.com/Mactarvish/vue-image-viewer) · 个人维护 · 中文 README

**基于 Vue2+Flask 的多文件夹 Web 看图工具**

基于 vue2 前端与 Flask 后端的 web 图片浏览工具，可在本地或远程服务器部署，支持一次浏览多个文件夹的图片，并可显示坐标与复制路径。面向深度学习与计算机视觉从业者快速查看和定位 case。使用时仅依赖 Python：安装 flask 与 Flask-Cors 后运行 backend/file_server.py，访问 http://127.0.0.1:8003 即可；前端二次开发需 npm install，发布版构建需通过 utils/build_vue.py 修改构建产物中的资源引用路径以便 Flask 加载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Flask 后端 + Vue2 前端，本地或远程服务器部署
- 支持多文件夹图片浏览、显示坐标、复制路径
- 运行仅需 Python 环境（flask、Flask-Cors），无需 node

## 适用场景

- 深度学习/CV 实验中快速浏览多个结果目录的图片
- 远程服务器上查看训练输出图片并定位 case
- 查看图片时获取像素坐标与文件路径

## 场景标签

 · 领域:计算机视觉/开发工具

## 证据(README 行号)

> L3: 基于vue2和flask的web看图工具，可在本地或远程服务器上部署。
> L5: 特别适用于深度学习和计算机视觉从业者看图/快速分析和定位case。

## 星数曲线

```mermaid
xychart-beta
    title "Mactarvish/vue-image-viewer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-27 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `7bf2dc92ce7b` · [字段定义](../../DATASET.md)*
