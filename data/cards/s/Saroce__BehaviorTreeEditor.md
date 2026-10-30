# Saroce/BehaviorTreeEditor

⭐ 46 · C# · MIT · 推送 2025-11-15 · [GitHub](https://github.com/Saroce/BehaviorTreeEditor) · 个人维护 · 中文 README

**Unity3D 行为树编辑器，Runtime 可脱离 Unity 供服务端使用**

基于 Unity UIToolkit 实现的行为树编辑器：编辑器部分（引用 Odin 插件）提供节点编辑、黑板、节点变量绑定、赋值粘贴、撤销回退、运行时预览、组合节点三种中断机制（Self/LowerPriority/Both）、Group 与 StickyNotes；数据以 Json 或 MemoryPack 序列化。Runtime 部分不引用任何 Unity API，可拷贝源码或生成 BTRuntime.dll 到服务端或帧同步框架工程使用；外部工程通过 ExternalCondition/ExternalAction 占位节点与 TypeName 映射在运行时替换重建树结构。限制：撤销重做仅支持节点数据，MemoryPack 跨程序集派生类需手动注册。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Runtime 不依赖 Unity API，可导出 BTRuntime.dll 供服务端/帧同步框架使用
- 支持 Json 与 MemoryPack 两种序列化格式
- 组合节点三种中断机制（Self/LowerPriority/Both）
- 外部节点占位（ExternalCondition/ExternalAction）运行时映射替换并重建树连接

## 适用场景

- 在 Unity 中编辑游戏 AI 行为树并挂载 BehaviorTree 组件运行
- 将行为树数据导出到服务端或帧同步框架复用同一套 Runtime
- 为外部工程节点类型做编辑期占位与运行时类型映射

## 场景标签

 · 领域:游戏开发/编辑器工具

## 证据(README 行号)

> L8:  - Runtime：注意Runtime部分需要支持脱离Unity环境运行，因此不能引用到任何Unity相关API和特性，用到了json序列化库**Newtonsoft.Json**和**MemoryPack**二进制存储方便序列化
> L13: 若只在Unity里面用，正常使用即可，挂载上BehaviorTree组件，或者其他反序列化BT数据后做Tick操作即可。当需要支持BT.Runtime部分脱离Unity环境运行，用于服务端或者帧同步框架上时，可以直接拷贝源码，或者
> L30: 增加了组合节点的中断功能，如图所示Sequence设置了LowPriority，当按钮按下时，能够打断右边的持续性Action节点运行，整体思路可参考BehaviorDesigner

## 星数曲线

```mermaid
xychart-beta
    title "Saroce/BehaviorTreeEditor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-30 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `20b238a5d43a` · [字段定义](../../DATASET.md)*
