# geospaitial-lab/aviary

⭐ 17 · Python · GPL-3.0 · 推送 2026-10-25 · [GitHub](https://github.com/geospaitial-lab/aviary) · [官网](https://geospaitial-lab.github.io/aviary) · 组织维护

**地理空间数据的 ML 推理模块化框架，少样板跑 AI 模型**

面向 Python 开发者的地理空间数据机器学习推理框架：通过可组合组件定义与运行流水线，提供高层 Python API 与配置驱动的 CLI 两种方式。支持插件注册表扩展自定义组件并打包分发。AI 框架无关，可使用 PyTorch、TensorFlow、ONNX 或 scikit-learn 的模型。要求 Python 3.10 及以上，提供 pip/uv 安装与 Docker 镜像，GPL-3.0 许可。

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

- 高层 Python API 以可组合组件定义流水线
- 配置驱动 CLI 以声明式配置运行同一流水线
- 插件注册表支持自定义组件并以插件包分发
- AI 框架无关：PyTorch/TensorFlow/ONNX/scikit-learn 模型可用

## 适用场景

- 在航空影像/正射影像等地理空间数据上运行 AI 模型
- 将快速原型的推理流水线复用为生产级流水线
- 以命令行加配置文件的方式批量执行推理任务

## 场景标签

`图像视频处理` `推理引擎` · 领域:感知与多模态

## 证据(README 行号)

> L12: aviary is the pythonic way to run your AI models on geospatial data
> L24: - **AI framework-agnostic**

## 星数曲线

```mermaid
xychart-beta
    title "geospaitial-lab/aviary 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `085c027cf332` · [字段定义](../../DATASET.md)*
