# vidispine/hull

⭐ 295 · Python · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/vidispine/hull) · [官网](https://hull.readthedocs.io/en/latest/) · 组织维护

**Helm 库图表：在 values.yaml 中直接定义 Kubernetes 对象**

HULL 是一个 Helm library chart，用于简化基于 Helm chart 的工作流：将 Kubernetes 对象及其属性完全在 values.yaml 中声明，省去编写自定义 YAML 模板文件，并提供 JSON schema 校验、统一可继承的对象元数据、ConfigMap/Secret 简化引入、values.yaml 内部交叉引用等功能。可作为依赖加入任意现有 chart 并存使用，不引入 Helm 之外的额外工具。版本与 Kubernetes 发布分支对齐，1.34.2/1.33.3/1.32.6 起兼容 Helm v4。面向使用 Helm 部署到 Kubernetes 的开发者与运维人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在 values.yaml 中完整声明 Kubernetes 对象，移除自定义模板层
- 基于 values.schema.json 的 JSON schema 校验
- 可作为依赖加入现有 Helm chart 并存使用，不引入额外工具
- 1.37.0 起默认 RBAC 三件套（ServiceAccount/Role/RoleBinding）改为 opt-in

## 适用场景

- 减少维护大量 Helm chart 模板文件的开销
- 用统一层快速定义部署、服务、ConfigMap、Ingress 等 Kubernetes 对象
- 以 values.yaml 覆盖文件在部署时切换配置

## 场景标签

 · 领域:云原生/DevOps 工具

## 证据(README 行号)

> L32: The primary feature of the HULL library is the ability to remove customized YAML template files entirely from Helm 
> L44: HULL remains compatible with existing Helm 3 releases and is fully compatible with Helm v4 starting with versions `
> L206: - `hull_validate.py` checks a chart and reports schema problems in the same format, and the Claude Code plugin and

## 星数曲线

```mermaid
xychart-beta
    title "vidispine/hull 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-10-25"]
    y-axis "stars" 294 --> 296
    line [295, 295]
```

2026-10-23 295 → 2026-10-25 295（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 low · 依据 README sha `676431054ed4` · [字段定义](../../DATASET.md)*
