# ZhiyuanChen/CHANfiG

⭐ 29 · Python · NOASSERTION · 推送 2026-10-19 · [GitHub](https://github.com/ZhiyuanChen/CHANfiG) · [官网](https://chanfig.danling.org) · 个人维护

**面向机器学习训练的 Python 配置管理库：命令行改配置**

继承 Python dict 实现的配置库，提供 FlatDict、DefaultDict、NestedDict、Config、Registry、Variable、ConfigParser 等组件。核心机制：属性式访问嵌套配置、${} 变量插值、命令行参数解析覆盖默认值、merge/difference/intersect 等操作、json/yaml 读写、类 PyTorch Tensor 的 to/cpu/gpu/tpu 设备转换、freeze/defrost 与 Registry 构建对象。兼容旧 json/yaml 配置与 YACS（替换 CfgNode 即可），从 PyPI 安装，多许可（含 Unlicense、AGPL v3）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- dict 属性式访问与嵌套结构遍历（all_keys/apply 等）
- ${} 变量插值与命令行参数覆盖默认配置
- 类 PyTorch 的 to/cpu/gpu/tpu 设备转换方法
- Registry 注册构造器并从 Config/dataclass 构建对象

## 适用场景

- 机器学习实验中用命令行快速修改训练参数
- 管理嵌套 json/yaml 配置文件并做合并与比较
- 兼容已有 YACS 配置的代码库迁移

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L18: There are tons of configurable parameters in training a Machine Learning model.
> L96: [`FlatDict`][chanfig.FlatDict] supports [`to`][chanfig.FlatDict.to] method similar to PyTorch Tensor.

## 星数曲线

```mermaid
xychart-beta
    title "ZhiyuanChen/CHANfiG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-28 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `cc57a454a256` · [字段定义](../../DATASET.md)*
