# cesium-ml/cesium_web

⭐ 46 · Python · NOASSERTION · 推送 2026-01-06 · [GitHub](https://github.com/cesium-ml/cesium_web) · 组织维护

**cesium 时间序列机器学习库的 Web 前端**

为 cesium 库提供的浏览器端 Web 前端：用户在网页中上传时间序列数据、提取特征、拟合模型，并对新数据生成预测。依赖 Supervisor、NGINX、PostgreSQL、Node.JS 等组件本地运行，也可通过 docker-compose 一键启动后访问 localhost:9000。支持多用户登录（Google 凭据）与配置文件自定义，要求 Python 3.6+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 浏览器内完成上传→特征提取→建模→预测流程
- 提供 docker-compose 一键运行方式
- 支持多用户登录与 Google 凭据配置
- 提供前端测试套件（ChromeDriver/Chrome）与 ESLint 代码规范

## 适用场景

- 在网页上对时间序列数据做机器学习建模与预测
- 不想写代码即可体验 cesium 库的分析流程
- 多用户环境下共享时间序列建模平台

## 场景标签

 · 领域:机器学习/时间序列分析

## 证据(README 行号)

> L8: the `cesium` library. Within
> L10: fit a model, and generate predictions for new data.

## 星数曲线

```mermaid
xychart-beta
    title "cesium-ml/cesium_web 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-28 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f3bcb323f4c3` · [字段定义](../../DATASET.md)*
