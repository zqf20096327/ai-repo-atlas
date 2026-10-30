# cortex1020/EvalLeak

⭐ 34 · Python · MIT · 推送 2026-09-05 · [GitHub](https://github.com/cortex1020/EvalLeak) · 个人维护

**检测训练/评估切分间数据污染的确定性 CLI 工具**

面向机器学习数据集构建与评测流程的污染检测工具：读取各 split 的行式文本 manifest，运行四类检查——跨切分精确重复（规范化摘要）、近似重复（字符 shingle + MinHash Jaccard 估计）、包含关系（评估条目嵌入训练长文档）、切分内重复；输出逐条记录 ID、方向性污染率与 CI 可用的退出码（0/1/2）。全部检查离线、确定性，仅依赖 Python 3.11 标准库，无第三方运行时依赖、无网络访问。规范化步骤（空白/大小写/标点）可分别关闭。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四类检测：精确重复、MinHash 近似重复、containment、切分内重复
- 输出方向性污染率与逐条记录 ID，可定位到具体记录
- 退出码 0/1/2 可直接用作 CI 门禁
- 仅用 Python 标准库，离线运行，输出字节级确定（无随机种子）

## 适用场景

- 训练前检查数据集 split 之间是否存在重叠污染
- 在 CI 中以退出码自动拦截被污染的评测集
- 发布数据集前做去重与卫生检查

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: EvalLeak detects contamination between training and evaluation splits by finding
> L49: Every check is offline, deterministic, and built on the Python standard library
> L173: |Code|Meaning|

## 星数曲线

```mermaid
xychart-beta
    title "cortex1020/EvalLeak 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-30"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-26 34 → 2026-10-30 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `f8d82f30dcfa` · [字段定义](../../DATASET.md)*
